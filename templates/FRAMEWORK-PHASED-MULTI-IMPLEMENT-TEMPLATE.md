# Phased Multi-Implement Template

Use this when the project is too large for a single `speckit-implement` run.

Replace all `{...}` placeholders.

How to use this file:

1. stabilize the artifacts with the pre-implement revision cycle
2. turn on strict phased mode
3. run one phase per `speckit-implement` prompt
4. validate each phase completely before the next one
5. do not let later-phase work leak into the current run
6. do not start any phase until `requirements.md` and `quality.md` are fully PASS
7. treat `generated/{FEATURE_ID}/phase-packs/*.md` as compiled artifacts, not canonical truth

## Canonical vs Derived Artifacts

Canonical truth for phased work lives in:

- `spec.md`
- `plan.md`
- `data-model.md`
- `contracts/*`
- `checklists/*`
- `tasks.md`
- `tasks.json`
- accepted `phase-summaries/*.json`

Derived phase packs live in:

- `generated/{FEATURE_ID}/phase-packs/*.md`
- `.speckit/feature-state.json`

If a phase changes canonical truth or accepts a new deviation:

1. update the canonical artifact first
2. write the accepted phase summary
3. run `python3 scripts/reconcile-phase-packs.py --root . --feature {FEATURE_ID}`
4. discard every older downstream phase pack
5. run `python3 scripts/verify-phase-pack-freshness.py --root . --feature {FEATURE_ID}`
6. only then start the next phase

## Pre-Implement Revision Cycle

```text
[$speckit-analyze]({REPO_PATH}/.agents/skills/speckit-analyze/SKILL.md) Review the current spec.md, plan.md, checklist artifacts, and tasks.md for missing coverage, contradictions, or drift before implementation.
```

```text
[$speckit-specify]({REPO_PATH}/.agents/skills/speckit-specify/SKILL.md) Revise the active spec to close the remaining analyze findings without broadening scope beyond the intended project.
```

```text
[$speckit-plan]({REPO_PATH}/.agents/skills/speckit-plan/SKILL.md) Revise the technical plan and derived design artifacts to close the remaining analyze findings and keep implementation-ready contracts, data model, and quickstart artifacts aligned.
```

```text
[$speckit-checklist]({REPO_PATH}/.agents/skills/speckit-checklist/SKILL.md) Refresh checklist artifacts from the revised spec and plan so the quality gates are current before task regeneration.

Create or refresh at minimum:
- `requirements.md`
- `quality.md`

Keep deeper domain-specific checklists too when the feature needs them.
```

```text
[$speckit-tasks]({REPO_PATH}/.agents/skills/speckit-tasks/SKILL.md) Regenerate tasks.md from the revised spec, plan, and checklist artifacts. Ensure every remaining issue has explicit implementation and verification coverage.
```

```text
[$speckit-checklist]({REPO_PATH}/.agents/skills/speckit-checklist/SKILL.md) Review spec.md, plan.md, tasks.md, and checklist artifacts before implementation.

Score `requirements.md` and `quality.md` completely:
- mark every checklist item PASS or FAIL
- cite the artifact that satisfies each PASS item
- do not leave any checklist item unchecked

If any checklist item is FAIL or unchecked:
- return BLOCKED
- list the exact failed items
- state whether spec.md, plan.md, or tasks.md must change
- do not recommend implementation
```

```text
[$speckit-analyze]({REPO_PATH}/.agents/skills/speckit-analyze/SKILL.md) Re-run analysis on the revised artifacts, including scored checklist coverage, and verify the remaining issues are closed before implementation begins.

Treat any FAIL or unchecked item in `requirements.md` or `quality.md` as a blocking issue.
```

## Strict Phased Mode

```text
[$speckit-implement]({REPO_PATH}/.agents/skills/speckit-implement/SKILL.md) For the active feature, work in strict phased mode for all subsequent implementation runs.

For every phase:
- read spec.md, plan.md, scored checklist artifacts, data-model.md, contracts/*, quickstart.md, and tasks.md before coding
- verify the phase pack `snapshot_id` still matches `.speckit/feature-state.json`
- identify the exact task IDs in scope for the phase plus any direct prerequisites
- implement only that dependency-closed set
- update task status in tasks.md as tasks are actually completed
- keep code, contracts, schema, docs, and tests aligned
- if the phase changes any canonical artifact, stop after the repair, reconcile the phase packs, and replace every downstream pack before continuing
- run lint, typecheck, tests, and build for every touched package before stopping
- end each phase with completed task IDs, files changed, validation run, blockers or follow-up risks, the accepted phase summary, and the next recommended phase
- if any checklist item is FAIL or unchecked, stop and return BLOCKED instead of asking to proceed anyway

Do not start later phases in this run.
```

## Single Phase Prompt

```text
[$speckit-implement]({REPO_PATH}/.agents/skills/speckit-implement/SKILL.md) Implement {PHASE_NAME} only for {FEATURE_ID}.

Before coding:
- confirm `generated/{FEATURE_ID}/phase-packs/{PHASE_ID}.md` has the same `snapshot_id` as `.speckit/feature-state.json`
- if the snapshot mismatches, stop and run `python3 scripts/reconcile-phase-packs.py --root . --feature {FEATURE_ID}`
- read spec.md, plan.md, scored checklist artifacts, data-model.md, contracts/*, quickstart.md, and tasks.md
- identify the exact task IDs for this phase and any prerequisites, then implement only that set

Phase scope:
- {PHASE_SCOPE_1}
- {PHASE_SCOPE_2}
- {PHASE_SCOPE_3}

Do not implement later phases in this run.

Stop and return BLOCKED if `requirements.md` or `quality.md` contains any FAIL or unchecked item.
If this phase changes canonical truth, stop after updating the source artifacts, write the accepted phase summary, reconcile the phase packs, and replace every downstream pack before continuing.

Validation required:
- {VALIDATION_1}
- {VALIDATION_2}
- {VALIDATION_3}
```
