# Kalshi Quant Dashboard Strict Phased Mode

Observed source: `/home/ai/.codex/history.jsonl`, session `019d7c0f-6eff-7920-85ac-aab67a3bc180`

Observed extra manual step immediately before this:

```text
create the dashboard.md first
```

Framework note:

- this preserved prompt shows what the dashboard run said at the time
- the current framework recommendation is to read checklist artifacts alongside `spec.md`, `plan.md`, and `tasks.md` before coding each phase

Back to [KALSHI-EXAMPLES.md](KALSHI-EXAMPLES.md)

Workflow this example follows:

- [FRAMEWORK-PHASED-MULTI-IMPLEMENT-TEMPLATE.md](../templates/FRAMEWORK-PHASED-MULTI-IMPLEMENT-TEMPLATE.md)

Dashboard read order:

1. [01 Initial Build](EXAMPLE-KALSHI-DASHBOARD-01-INITIAL-BUILD.md)
2. [02 Pre-Implement Revision](EXAMPLE-KALSHI-DASHBOARD-02-PRE-IMPLEMENT-REVISION.md)
3. `03 Strict Phased Mode` <- you are here
4. [04 Phase 2 Prompt](EXAMPLE-KALSHI-DASHBOARD-04-PHASE-2.md)
5. [05 Phase 3 Prompt](EXAMPLE-KALSHI-DASHBOARD-05-PHASE-3.md)
6. [06 Phase 4 Prompt](EXAMPLE-KALSHI-DASHBOARD-06-PHASE-4.md)

What this file captures:

- the global phased-mode instruction that must be set before the per-phase prompts
- the rule that every phase is dependency-closed and validated before moving on

Note:

- the preserved individual phase prompts in this repo start at Phase 2
- a separate Phase 1 prompt was not preserved in the history snapshot used for this corpus

Previous file:

- [EXAMPLE-KALSHI-DASHBOARD-02-PRE-IMPLEMENT-REVISION.md](EXAMPLE-KALSHI-DASHBOARD-02-PRE-IMPLEMENT-REVISION.md)

Next file:

- [EXAMPLE-KALSHI-DASHBOARD-04-PHASE-2.md](EXAMPLE-KALSHI-DASHBOARD-04-PHASE-2.md)

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
