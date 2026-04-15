<!-- SPECKIT_PHASE_PACK
{
  "feature_id": "001-quant-ops-dashboard",
  "phase_id": "pre-implement-revision",
  "phase_name": "Pre-Implement Revision",
  "snapshot_id": "sha256:5d60be175b9f7efef8660592afaf62ac771536b5a24ac55a8720ffed7ca248b1",
  "phase_index": 2,
  "phase_count": 6,
  "kind": "artifact_repair",
  "depends_on_phases": [
    "initial-build"
  ],
  "task_ids": [],
  "dependency_task_ids": [],
  "accepted_summary_ids": [
    "initial-build"
  ],
  "compiler": "scripts/reconcile-phase-packs.py"
}
-->

# Compiled Phase Pack: Pre-Implement Revision

This file is derived. Do not edit it by hand.

- feature: `001-quant-ops-dashboard`
- phase: `pre-implement-revision`
- snapshot_id: `sha256:5d60be175b9f7efef8660592afaf62ac771536b5a24ac55a8720ffed7ca248b1`
- freshness rule: the pack is invalid if `.speckit/feature-state.json` reports a different `latest_snapshot_id`

## Canonical Inputs

- `spec.md`
- `plan.md`
- `data-model.md`
- `quickstart.md`
- `contracts/*`
- `checklists/*`
- `tasks.md`
- `tasks.json`
- `accepted phase summaries`

## Phase Scope

- Run the analyze -> revise spec -> revise plan -> refresh checklist -> regenerate tasks -> score checklists -> analyze again loop.
- Close contradictions before any implementation prompt is allowed.

## Phase Dependencies

- `initial-build`

## Task Set

- direct: `none`

## Accepted Upstream Deviations

- Preserved a phased implementation strategy instead of a single broad implementation run.

## Validation Required

- requirements.md is fully PASS.
- quality.md is fully PASS.
- analyze no longer reports blocking contradictions.

## Reconciliation Rule

If this phase changes any canonical artifact or accepts a new deviation:

1. update the canonical artifact first
2. write the accepted phase summary
3. run `python3 scripts/reconcile-phase-packs.py --root . --feature 001-quant-ops-dashboard`
4. discard every older downstream phase pack

