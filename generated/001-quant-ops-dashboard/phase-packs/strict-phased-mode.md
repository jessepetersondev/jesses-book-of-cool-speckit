<!-- SPECKIT_PHASE_PACK
{
  "feature_id": "001-quant-ops-dashboard",
  "phase_id": "strict-phased-mode",
  "phase_name": "Strict Phased Mode",
  "snapshot_id": "sha256:5d60be175b9f7efef8660592afaf62ac771536b5a24ac55a8720ffed7ca248b1",
  "phase_index": 3,
  "phase_count": 6,
  "kind": "mode_lock",
  "depends_on_phases": [
    "pre-implement-revision"
  ],
  "task_ids": [],
  "dependency_task_ids": [],
  "accepted_summary_ids": [
    "initial-build",
    "pre-implement-revision"
  ],
  "compiler": "scripts/reconcile-phase-packs.py"
}
-->

# Compiled Phase Pack: Strict Phased Mode

This file is derived. Do not edit it by hand.

- feature: `001-quant-ops-dashboard`
- phase: `strict-phased-mode`
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

- Lock the backend-first phase order so implementation stays dependency-closed.
- Refuse later-phase work in the current run.

## Phase Dependencies

- `pre-implement-revision`

## Task Set

- direct: `none`

## Accepted Upstream Deviations

- Preserved a phased implementation strategy instead of a single broad implementation run.
- Kept the dashboard focused on operator-critical routes before broader analytics.

## Validation Required

- Every implementation pack names exact task IDs and validation gates.
- No phase prompt includes later-phase UI work by default.

## Reconciliation Rule

If this phase changes any canonical artifact or accepts a new deviation:

1. update the canonical artifact first
2. write the accepted phase summary
3. run `python3 scripts/reconcile-phase-packs.py --root . --feature 001-quant-ops-dashboard`
4. discard every older downstream phase pack

