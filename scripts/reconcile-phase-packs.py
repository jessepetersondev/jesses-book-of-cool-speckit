#!/usr/bin/env python3
"""Compile phase packs from canonical SpecKit artifacts."""

from __future__ import annotations

import argparse
from pathlib import Path

from _phase_pack_lib import (
    PhasePackError,
    build_pack_metadata,
    build_state_entry,
    dump_json,
    feature_ids,
    load_feature_bundle,
    load_state,
    render_pack,
    state_path,
    write_pack,
)


def reconcile_feature(root: Path, feature_id: str) -> dict:
    bundle = load_feature_bundle(root, feature_id)
    pack_dir = root / "generated" / feature_id / "phase-packs"

    for phase_index, phase in enumerate(bundle["phases"], start=1):
        metadata = build_pack_metadata(bundle, phase, phase_index)
        output_path = pack_dir / f"{phase['phase_id']}.md"
        write_pack(output_path, render_pack(bundle, phase, metadata))

    return build_state_entry(root, bundle)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compile phase packs from canonical SpecKit artifacts.",
    )
    parser.add_argument("--root", default=".", help="Repo root containing specs/, generated/, and .speckit/")
    parser.add_argument("--feature", help="Reconcile only one feature id")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    features = feature_ids(root, args.feature)
    if not features:
        print(f"No phase plans found under {root / 'specs'}")
        return 0

    try:
        state = load_state(root)
        by_feature = {entry["feature_id"]: entry for entry in state.get("features", [])}

        for feature_id in features:
            by_feature[feature_id] = reconcile_feature(root, feature_id)
            print(f"reconciled {feature_id}")

        next_state = {
            "version": 1,
            "features": [by_feature[feature_id] for feature_id in sorted(by_feature)],
        }
        dump_json(state_path(root), next_state)
    except PhasePackError as exc:
        print(f"ERROR: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
