<!-- SPECKIT_PHASE_PACK
{
  "feature_id": "001-quant-ops-dashboard",
  "phase_id": "initial-build",
  "phase_name": "Initial Build",
  "snapshot_id": "sha256:5d60be175b9f7efef8660592afaf62ac771536b5a24ac55a8720ffed7ca248b1",
  "phase_index": 1,
  "phase_count": 6,
  "kind": "artifact_build",
  "depends_on_phases": [],
  "task_ids": [],
  "dependency_task_ids": [],
  "accepted_summary_ids": [],
  "compiler": "scripts/reconcile-phase-packs.py"
}
-->

# Compiled Phase Pack: Initial Build

This file is derived. Do not edit it by hand.

- feature: `001-quant-ops-dashboard`
- phase: `initial-build`
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

- Generate spec.md, plan.md, data-model.md, contracts, checklists, and tasks from the large product request.
- Keep the system narrow enough that later analyze passes can still repair it safely.

## Phase Dependencies

- `none`

## Task Set

- direct: `none`

## Accepted Upstream Deviations

- none

## Validation Required

- Core artifacts exist and describe the same product.
- The initial task graph is specific enough to review before coding.

## Reconciliation Rule

If this phase changes any canonical artifact or accepts a new deviation:

1. update the canonical artifact first
2. write the accepted phase summary
3. run `python3 scripts/reconcile-phase-packs.py --root . --feature 001-quant-ops-dashboard`
4. discard every older downstream phase pack

