# Generated Dashboard Prompt Pack

- stage: strict_phased_mode
- source_example: [../../EXAMPLE-KALSHI-DASHBOARD-03-STRICT-PHASED-MODE.md](../../EXAMPLE-KALSHI-DASHBOARD-03-STRICT-PHASED-MODE.md)
- generated_at: 2026-04-12
- repo_path: /home/ai/clawd/projects/kalshi-quant-dashboard
- feature_id: 001-quant-ops-dashboard
- preserved_prompt_count: 2

# Strict Phased Mode Pack

Use this pack immediately after the revision loop passes. It records the manual precondition and the exact phased-mode lock that preceded the later implementation runs.

## Manual Precondition

```text
create the dashboard.md first
```

## Strict Phased Mode Prompt

```text
[$speckit-implement](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-implement/SKILL.md) For the active 001-quant-ops-dashboard feature, work in strict phased mode for all subsequent implementation runs.

For every phase:
- Read spec.md, plan.md, checklist artifacts, data-model.md, contracts/*, quickstart.md, and tasks.md before coding.
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
