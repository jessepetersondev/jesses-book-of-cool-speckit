# Kalshi Quant Dashboard Strict Phased Mode

Observed source: `/home/ai/.codex/history.jsonl`, session `019d7c0f-6eff-7920-85ac-aab67a3bc180`

Observed extra manual step immediately before this:

```text
create the dashboard.md first
```

## Prompt

```text
[$speckit-implement](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-implement/SKILL.md) For the active 001-quant-ops-dashboard feature, work in strict phased mode for all subsequent implementation runs.

For every phase:
- Read spec.md, plan.md, data-model.md, contracts/*, quickstart.md, and tasks.md before coding.
- Identify the exact task IDs in scope for the phase plus any direct prerequisite tasks. List them first.
- Implement only that dependency-closed set. Do not jump ahead.
- Update task status in tasks.md as tasks are actually completed.
- Keep code, contracts, schema, docs, and tests aligned. Do not leave TODOs, placeholders, fake health data, or mock-only production paths.
- Run lint, typecheck, tests, and build for every touched package before stopping.
- End each phase with:
  1. completed task IDs
  2. files changed
  3. validation run
  4. blockers or follow-up risks
  5. the next recommended phase

Do not start later phases in this run. Use the current spec and plan as the source of truth.
```
