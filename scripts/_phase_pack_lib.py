#!/usr/bin/env python3
"""Shared helpers for reconciling and verifying SpecKit phase packs."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any


PACK_METADATA_PATTERN = re.compile(
    r"<!--\s*SPECKIT_PHASE_PACK\s*(\{.*?\})\s*-->",
    re.DOTALL,
)


class PhasePackError(RuntimeError):
    """Raised when the phase-pack fixture is incomplete or inconsistent."""


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def stable_json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def feature_ids(root: Path, requested_feature: str | None = None) -> list[str]:
    specs_root = root / "specs"
    if requested_feature:
        return [requested_feature] if (specs_root / requested_feature / "phase-plan.json").exists() else []
    if not specs_root.exists():
        return []
    feature_dirs = sorted(path for path in specs_root.iterdir() if path.is_dir())
    return [path.name for path in feature_dirs if (path / "phase-plan.json").exists()]


def require_paths(root: Path, feature_id: str) -> dict[str, Path]:
    feature_root = root / "specs" / feature_id
    required = {
        "feature_root": feature_root,
        "spec": feature_root / "spec.md",
        "plan": feature_root / "plan.md",
        "data_model": feature_root / "data-model.md",
        "quickstart": feature_root / "quickstart.md",
        "phase_plan": feature_root / "phase-plan.json",
        "tasks_markdown": feature_root / "tasks.md",
        "tasks": feature_root / "tasks.json",
        "contracts_dir": feature_root / "contracts",
        "checklists_dir": feature_root / "checklists",
        "phase_summaries_dir": feature_root / "phase-summaries",
    }

    missing = [
        name
        for name, path in required.items()
        if name.endswith("_dir") and not path.is_dir()
        or not name.endswith("_dir") and not path.exists()
    ]
    if missing:
        joined = ", ".join(sorted(missing))
        raise PhasePackError(f"{feature_id}: missing required canonical artifacts: {joined}")

    if not any(path.is_file() for path in required["contracts_dir"].rglob("*")):
        raise PhasePackError(f"{feature_id}: contracts/ must contain at least one file")
    if not any(path.is_file() for path in required["checklists_dir"].rglob("*")):
        raise PhasePackError(f"{feature_id}: checklists/ must contain at least one file")
    if not any(path.is_file() for path in required["phase_summaries_dir"].glob("*.json")):
        raise PhasePackError(f"{feature_id}: phase-summaries/ must contain at least one summary")

    return required


def load_feature_bundle(root: Path, feature_id: str) -> dict[str, Any]:
    paths = require_paths(root, feature_id)
    phase_plan = load_json(paths["phase_plan"])
    tasks_doc = load_json(paths["tasks"])
    phase_summaries = [
        {"path": path, "data": load_json(path)}
        for path in sorted(paths["phase_summaries_dir"].glob("*.json"))
    ]

    accepted_summaries = [
        summary for summary in phase_summaries if summary["data"].get("status") == "accepted"
    ]
    if not accepted_summaries:
        raise PhasePackError(f"{feature_id}: at least one accepted phase summary is required")

    phases = sorted(phase_plan.get("phases", []), key=lambda item: item["order"])
    if not phases:
        raise PhasePackError(f"{feature_id}: phase-plan.json must define at least one phase")

    order_map = {phase["phase_id"]: phase["order"] for phase in phases}
    tasks_by_id = {task["task_id"]: task for task in tasks_doc.get("tasks", [])}
    tasks_by_phase: dict[str, list[dict[str, Any]]] = {}
    for task in tasks_doc.get("tasks", []):
        tasks_by_phase.setdefault(task["phase_id"], []).append(task)

    canonical_paths = canonical_artifact_paths(root, feature_id)
    snapshot_id = compute_snapshot_id(root, canonical_paths, accepted_summaries)

    return {
        "feature_id": feature_id,
        "paths": paths,
        "phase_plan": phase_plan,
        "phases": phases,
        "phase_order_map": order_map,
        "tasks_doc": tasks_doc,
        "tasks_by_id": tasks_by_id,
        "tasks_by_phase": tasks_by_phase,
        "phase_summaries": phase_summaries,
        "accepted_summaries": accepted_summaries,
        "canonical_paths": canonical_paths,
        "snapshot_id": snapshot_id,
    }


def canonical_artifact_paths(root: Path, feature_id: str) -> list[Path]:
    feature_root = root / "specs" / feature_id
    paths = [
        feature_root / "spec.md",
        feature_root / "plan.md",
        feature_root / "data-model.md",
        feature_root / "quickstart.md",
        feature_root / "phase-plan.json",
        feature_root / "tasks.md",
        feature_root / "tasks.json",
    ]

    for dirname in ("contracts", "checklists"):
        base = feature_root / dirname
        paths.extend(sorted(path for path in base.rglob("*") if path.is_file()))

    return sorted(paths)


def compute_snapshot_id(
    root: Path,
    canonical_paths: list[Path],
    accepted_summaries: list[dict[str, Any]],
) -> str:
    hasher = hashlib.sha256()

    for path in canonical_paths:
        rel = path.relative_to(root).as_posix()
        hasher.update(rel.encode("utf-8"))
        hasher.update(b"\0")
        hasher.update(path.read_bytes())
        hasher.update(b"\0")

    for summary in accepted_summaries:
        rel = summary["path"].relative_to(root).as_posix()
        hasher.update(rel.encode("utf-8"))
        hasher.update(b"\0")
        hasher.update(stable_json_text(summary["data"]).encode("utf-8"))
        hasher.update(b"\0")

    return f"sha256:{hasher.hexdigest()}"


def dependency_closure(task_ids: list[str], tasks_by_id: dict[str, dict[str, Any]]) -> list[str]:
    closure: set[str] = set()
    stack = list(task_ids)
    while stack:
        task_id = stack.pop()
        if task_id in closure:
            continue
        task = tasks_by_id.get(task_id)
        if task is None:
            raise PhasePackError(f"unknown task dependency: {task_id}")
        closure.add(task_id)
        stack.extend(task.get("depends_on", []))
    return sorted(closure)


def accepted_summaries_before_phase(bundle: dict[str, Any], phase_id: str) -> list[dict[str, Any]]:
    current_order = bundle["phase_order_map"][phase_id]
    accepted = []
    for summary in bundle["accepted_summaries"]:
        summary_phase = summary["data"]["phase_id"]
        summary_order = bundle["phase_order_map"].get(summary_phase)
        if summary_order is not None and summary_order < current_order:
            accepted.append(summary)
    return sorted(
        accepted,
        key=lambda item: bundle["phase_order_map"].get(item["data"]["phase_id"], 0),
    )


def build_pack_metadata(bundle: dict[str, Any], phase: dict[str, Any], phase_index: int) -> dict[str, Any]:
    direct_tasks = [
        task["task_id"]
        for task in sorted(
            bundle["tasks_by_phase"].get(phase["phase_id"], []),
            key=lambda item: item["task_id"],
        )
    ]
    closure = dependency_closure(direct_tasks, bundle["tasks_by_id"]) if direct_tasks else []
    dependency_tasks = [task_id for task_id in closure if task_id not in set(direct_tasks)]
    accepted_inputs = accepted_summaries_before_phase(bundle, phase["phase_id"])

    return {
        "feature_id": bundle["feature_id"],
        "phase_id": phase["phase_id"],
        "phase_name": phase["name"],
        "snapshot_id": bundle["snapshot_id"],
        "phase_index": phase_index,
        "phase_count": len(bundle["phases"]),
        "kind": phase["kind"],
        "depends_on_phases": phase.get("depends_on_phases", []),
        "task_ids": direct_tasks,
        "dependency_task_ids": dependency_tasks,
        "accepted_summary_ids": [summary["data"]["phase_id"] for summary in accepted_inputs],
        "compiler": "scripts/reconcile-phase-packs.py",
    }


def render_pack(bundle: dict[str, Any], phase: dict[str, Any], metadata: dict[str, Any]) -> str:
    accepted_inputs = accepted_summaries_before_phase(bundle, phase["phase_id"])
    accepted_deviations: list[str] = []
    for summary in accepted_inputs:
        accepted_deviations.extend(summary["data"].get("accepted_deviations", []))

    canonical_refs = [
        "spec.md",
        "plan.md",
        "data-model.md",
        "quickstart.md",
        "contracts/*",
        "checklists/*",
        "tasks.md",
        "tasks.json",
        "accepted phase summaries",
    ]

    lines = [
        "<!-- SPECKIT_PHASE_PACK",
        json.dumps(metadata, indent=2),
        "-->",
        "",
        f"# Compiled Phase Pack: {phase['name']}",
        "",
        "This file is derived. Do not edit it by hand.",
        "",
        f"- feature: `{bundle['feature_id']}`",
        f"- phase: `{phase['phase_id']}`",
        f"- snapshot_id: `{bundle['snapshot_id']}`",
        "- freshness rule: the pack is invalid if `.speckit/feature-state.json` reports a different `latest_snapshot_id`",
        "",
        "## Canonical Inputs",
        "",
    ]
    lines.extend(f"- `{item}`" for item in canonical_refs)
    lines.extend(
        [
            "",
            "## Phase Scope",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in phase.get("scope", []))

    lines.extend(
        [
            "",
            "## Phase Dependencies",
            "",
        ]
    )
    dependency_phases = metadata["depends_on_phases"] or ["none"]
    lines.extend(f"- `{item}`" for item in dependency_phases)

    lines.extend(
        [
            "",
            "## Task Set",
            "",
        ]
    )
    if metadata["task_ids"]:
        lines.extend(f"- direct: `{task_id}`" for task_id in metadata["task_ids"])
    else:
        lines.append("- direct: `none`")
    if metadata["dependency_task_ids"]:
        lines.extend(f"- prerequisite: `{task_id}`" for task_id in metadata["dependency_task_ids"])

    lines.extend(
        [
            "",
            "## Accepted Upstream Deviations",
            "",
        ]
    )
    if accepted_deviations:
        lines.extend(f"- {item}" for item in accepted_deviations)
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Validation Required",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in phase.get("validation", []))
    lines.extend(
        [
            "",
            "## Reconciliation Rule",
            "",
            "If this phase changes any canonical artifact or accepts a new deviation:",
            "",
            "1. update the canonical artifact first",
            "2. write the accepted phase summary",
            "3. run `python3 scripts/reconcile-phase-packs.py --root . --feature "
            f"{bundle['feature_id']}`",
            "4. discard every older downstream phase pack",
            "",
        ]
    )
    return "\n".join(lines)


def state_path(root: Path) -> Path:
    return root / ".speckit" / "feature-state.json"


def load_state(root: Path) -> dict[str, Any]:
    path = state_path(root)
    if not path.exists():
        return {"version": 1, "features": []}
    return load_json(path)


def build_state_entry(root: Path, bundle: dict[str, Any]) -> dict[str, Any]:
    pack_dir = Path("generated") / bundle["feature_id"] / "phase-packs"
    packs = []
    for phase_index, phase in enumerate(bundle["phases"], start=1):
        metadata = build_pack_metadata(bundle, phase, phase_index)
        packs.append(
            {
                "phase_id": phase["phase_id"],
                "path": (pack_dir / f"{phase['phase_id']}.md").as_posix(),
                "snapshot_id": bundle["snapshot_id"],
                "task_ids": metadata["task_ids"],
                "dependency_task_ids": metadata["dependency_task_ids"],
            }
        )

    accepted_ids = [
        summary["data"]["phase_id"]
        for summary in sorted(
            bundle["accepted_summaries"],
            key=lambda item: bundle["phase_order_map"].get(item["data"]["phase_id"], 0),
        )
    ]

    return {
        "feature_id": bundle["feature_id"],
        "latest_snapshot_id": bundle["snapshot_id"],
        "canonical_artifacts": [path.relative_to(root).as_posix() for path in bundle["canonical_paths"]],
        "accepted_phase_summaries": accepted_ids,
        "phase_plan_path": f"specs/{bundle['feature_id']}/phase-plan.json",
        "tasks_path": f"specs/{bundle['feature_id']}/tasks.json",
        "phase_summary_dir": f"specs/{bundle['feature_id']}/phase-summaries",
        "generated_pack_dir": f"generated/{bundle['feature_id']}/phase-packs",
        "phase_packs": packs,
    }


def write_pack(path: Path, contents: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(contents + "\n", encoding="utf-8")


def parse_pack_metadata(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = PACK_METADATA_PATTERN.search(text)
    if match is None:
        raise PhasePackError(f"{path}: missing SPECKIT_PHASE_PACK metadata block")
    return json.loads(match.group(1))
