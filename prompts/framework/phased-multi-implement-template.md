# Phased Multi-Implement Template

Use this when the project is too large for a single `speckit-implement` run.

Replace all `{...}` placeholders.

## Pre-Implement Revision Cycle

```text
[$speckit-analyze]({REPO_PATH}/.agents/skills/speckit-analyze/SKILL.md) Review the current spec.md, plan.md, and tasks.md for missing coverage, contradictions, or drift before implementation.
```

```text
[$speckit-specify]({REPO_PATH}/.agents/skills/speckit-specify/SKILL.md) Revise the active spec to close the remaining analyze findings without broadening scope beyond the intended project.
```

```text
[$speckit-plan]({REPO_PATH}/.agents/skills/speckit-plan/SKILL.md) Revise the technical plan and derived design artifacts to close the remaining analyze findings and keep implementation-ready contracts, data model, and quickstart artifacts aligned.
```

```text
[$speckit-tasks]({REPO_PATH}/.agents/skills/speckit-tasks/SKILL.md) Regenerate tasks.md from the revised spec and plan. Ensure every remaining issue has explicit implementation and verification coverage.
```

```text
[$speckit-analyze]({REPO_PATH}/.agents/skills/speckit-analyze/SKILL.md) Re-run analysis on the revised artifacts and verify the remaining issues are closed before implementation begins.
```

## Strict Phased Mode

```text
[$speckit-implement]({REPO_PATH}/.agents/skills/speckit-implement/SKILL.md) For the active feature, work in strict phased mode for all subsequent implementation runs.

For every phase:
- read spec.md, plan.md, data-model.md, contracts/*, quickstart.md, and tasks.md before coding
- identify the exact task IDs in scope for the phase plus any direct prerequisites
- implement only that dependency-closed set
- update task status in tasks.md as tasks are actually completed
- keep code, contracts, schema, docs, and tests aligned
- run lint, typecheck, tests, and build for every touched package before stopping
- end each phase with completed task IDs, files changed, validation run, blockers or follow-up risks, and the next recommended phase

Do not start later phases in this run.
```

## Single Phase Prompt

```text
[$speckit-implement]({REPO_PATH}/.agents/skills/speckit-implement/SKILL.md) Implement {PHASE_NAME} only for {FEATURE_ID}.

Before coding, read spec.md, plan.md, data-model.md, contracts/*, quickstart.md, and tasks.md. Identify the exact task IDs for this phase and any prerequisites, then implement only that set.

Phase scope:
- {PHASE_SCOPE_1}
- {PHASE_SCOPE_2}
- {PHASE_SCOPE_3}

Do not implement later phases in this run.

Validation required:
- {VALIDATION_1}
- {VALIDATION_2}
- {VALIDATION_3}
```
