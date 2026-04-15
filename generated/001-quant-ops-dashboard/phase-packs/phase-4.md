<!-- SPECKIT_PHASE_PACK
{
  "feature_id": "001-quant-ops-dashboard",
  "phase_id": "phase-4",
  "phase_name": "Phase 4",
  "snapshot_id": "sha256:5d60be175b9f7efef8660592afaf62ac771536b5a24ac55a8720ffed7ca248b1",
  "phase_index": 6,
  "phase_count": 6,
  "kind": "implementation",
  "depends_on_phases": [
    "phase-3"
  ],
  "task_ids": [
    "DASH-401",
    "DASH-402",
    "DASH-403"
  ],
  "dependency_task_ids": [
    "DASH-201",
    "DASH-202",
    "DASH-203",
    "DASH-301",
    "DASH-302",
    "DASH-303"
  ],
  "accepted_summary_ids": [
    "initial-build",
    "pre-implement-revision",
    "strict-phased-mode",
    "phase-2",
    "phase-3"
  ],
  "compiler": "scripts/reconcile-phase-packs.py"
}
-->

# Compiled Phase Pack: Phase 4

This file is derived. Do not edit it by hand.

- feature: `001-quant-ops-dashboard`
- phase: `phase-4`
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

- Implement the operator React UI, route map, live wiring, and degraded-state handling.
- Build only on top of the validated backend contracts and SSE layer.

## Phase Dependencies

- `phase-3`

## Task Set

- direct: `DASH-401`
- direct: `DASH-402`
- direct: `DASH-403`
- prerequisite: `DASH-201`
- prerequisite: `DASH-202`
- prerequisite: `DASH-203`
- prerequisite: `DASH-301`
- prerequisite: `DASH-302`
- prerequisite: `DASH-303`

## Accepted Upstream Deviations

- Preserved a phased implementation strategy instead of a single broad implementation run.
- Kept the dashboard focused on operator-critical routes before broader analytics.
- UI work remained blocked until backend contracts and SSE enforcement validated cleanly.
- Preserved backend-first sequencing before any operator UI wiring.
- Locked the SSE authorization surface before phase-4 UI work.

## Validation Required

- The web app builds cleanly.
- Route-level and operator-journey tests pass.
- No page depends on mocked production data.

## Reconciliation Rule

If this phase changes any canonical artifact or accepts a new deviation:

1. update the canonical artifact first
2. write the accepted phase summary
3. run `python3 scripts/reconcile-phase-packs.py --root . --feature 001-quant-ops-dashboard`
4. discard every older downstream phase pack

