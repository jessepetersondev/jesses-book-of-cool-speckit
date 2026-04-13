# Generated Prompt Pack

- workflow: phased
- template: templates/FRAMEWORK-PHASED-MULTI-IMPLEMENT-TEMPLATE.md
- generated_at: 2026-04-13
- repo_path: /home/ai/clawd/projects/kalshi-quant-dashboard
- unresolved_placeholders: none

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

## Pre-Implement Revision Cycle

```text
[$speckit-analyze](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-analyze/SKILL.md) Review the current spec.md, plan.md, checklist artifacts, and tasks.md for missing coverage, contradictions, or drift before implementation.
```

```text
[$speckit-specify](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-specify/SKILL.md) Revise the active spec to close the remaining analyze findings without broadening scope beyond the intended project.
```

```text
[$speckit-plan](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-plan/SKILL.md) Revise the technical plan and derived design artifacts to close the remaining analyze findings and keep implementation-ready contracts, data model, and quickstart artifacts aligned.
```

```text
[$speckit-checklist](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-checklist/SKILL.md) Refresh checklist artifacts from the revised spec and plan so the quality gates are current before task regeneration.

Create or refresh at minimum:
- `requirements.md`
- `quality.md`

Keep deeper domain-specific checklists too when the feature needs them.
```

```text
[$speckit-tasks](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-tasks/SKILL.md) Regenerate tasks.md from the revised spec, plan, and checklist artifacts. Ensure every remaining issue has explicit implementation and verification coverage.
```

```text
[$speckit-checklist](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-checklist/SKILL.md) Review spec.md, plan.md, tasks.md, and checklist artifacts before implementation.

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
[$speckit-analyze](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-analyze/SKILL.md) Re-run analysis on the revised artifacts, including scored checklist coverage, and verify the remaining issues are closed before implementation begins.

Treat any FAIL or unchecked item in `requirements.md` or `quality.md` as a blocking issue.
```

## Strict Phased Mode

```text
[$speckit-implement](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-implement/SKILL.md) For the active feature, work in strict phased mode for all subsequent implementation runs.

For every phase:
- read spec.md, plan.md, scored checklist artifacts, data-model.md, contracts/*, quickstart.md, and tasks.md before coding
- identify the exact task IDs in scope for the phase plus any direct prerequisites
- implement only that dependency-closed set
- update task status in tasks.md as tasks are actually completed
- keep code, contracts, schema, docs, and tests aligned
- run lint, typecheck, tests, and build for every touched package before stopping
- end each phase with completed task IDs, files changed, validation run, blockers or follow-up risks, and the next recommended phase
- if any checklist item is FAIL or unchecked, stop and return BLOCKED instead of asking to proceed anyway

Do not start later phases in this run.
```

## Single Phase Prompt

```text
[$speckit-implement](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-implement/SKILL.md) Implement Phase 2 only for 001-quant-ops-dashboard.

Before coding, read spec.md, plan.md, scored checklist artifacts, data-model.md, contracts/*, quickstart.md, and tasks.md. Identify the exact task IDs for this phase and any prerequisites, then implement only that set.

Phase scope:
- Implement the canonical normalized event model in code and schema.
- Implement mixed-source ingestion adapters, durable persistence, and replay-safe convergence.
- Do not implement the full operator UI in this run.

Do not implement later phases in this run.

Stop and return BLOCKED if `requirements.md` or `quality.md` contains any FAIL or unchecked item.

Validation required:
- migration and schema updates pass
- ingestion integration tests pass against representative fixtures
- replay/redelivery tests prove ordered convergence
```
