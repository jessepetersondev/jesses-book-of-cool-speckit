#!/usr/bin/env python3
"""Verify that committed phase packs match the latest canonical snapshot."""

from __future__ import annotations

import argparse
from pathlib import Path

from _phase_pack_lib import (
    PhasePackError,
    build_state_entry,
    feature_ids,
    load_feature_bundle,
    load_state,
    parse_pack_metadata,
)


def verify_feature(root: Path, feature_id: str, state_by_feature: dict[str, dict]) -> list[str]:
    issues: list[str] = []
    bundle = load_feature_bundle(root, feature_id)
    expected_state = build_state_entry(root, bundle)
    actual_state = state_by_feature.get(feature_id)

    if actual_state is None:
        issues.append(f"{feature_id}: missing .speckit state entry")
        return issues

    if actual_state.get("latest_snapshot_id") != bundle["snapshot_id"]:
        issues.append(
            f"{feature_id}: latest_snapshot_id mismatch "
            f"({actual_state.get('latest_snapshot_id')} != {bundle['snapshot_id']})"
        )

    if actual_state != expected_state:
        issues.append(f"{feature_id}: .speckit state entry is out of date")

    for pack in expected_state["phase_packs"]:
        pack_path = root / pack["path"]
        if not pack_path.exists():
            issues.append(f"{feature_id}: missing compiled pack {pack['path']}")
            continue

        metadata = parse_pack_metadata(pack_path)
        if metadata.get("feature_id") != feature_id:
            issues.append(f"{feature_id}: {pack['path']} has wrong feature_id")
        if metadata.get("phase_id") != pack["phase_id"]:
            issues.append(f"{feature_id}: {pack['path']} has wrong phase_id")
        if metadata.get("snapshot_id") != bundle["snapshot_id"]:
            issues.append(
                f"{feature_id}: {pack['path']} snapshot_id "
                f"{metadata.get('snapshot_id')} does not match {bundle['snapshot_id']}"
            )
        if metadata.get("task_ids") != pack["task_ids"]:
            issues.append(f"{feature_id}: {pack['path']} task_ids drifted")
        if metadata.get("dependency_task_ids") != pack["dependency_task_ids"]:
            issues.append(f"{feature_id}: {pack['path']} dependency_task_ids drifted")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify that phase packs match the latest canonical snapshot.",
    )
    parser.add_argument("--root", default=".", help="Repo root containing specs/, generated/, and .speckit/")
    parser.add_argument("--feature", help="Verify only one feature id")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    features = feature_ids(root, args.feature)
    if not features:
        print(f"No phase plans found under {root / 'specs'}")
        return 0

    state = load_state(root)
    state_by_feature = {entry["feature_id"]: entry for entry in state.get("features", [])}

    issues: list[str] = []
    try:
        for feature_id in features:
            issues.extend(verify_feature(root, feature_id, state_by_feature))
    except PhasePackError as exc:
        issues.append(str(exc))

    if issues:
        for issue in issues:
            print(f"ERROR: {issue}")
        return 1

    print(f"verified {len(features)} feature(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
