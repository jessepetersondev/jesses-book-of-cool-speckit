# Kalshi Quant Dashboard Phase 4 Prompt

Observed source: `/home/ai/.codex/history.jsonl`, session `019d7c0f-6eff-7920-85ac-aab67a3bc180`

```text
[$speckit-implement](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-implement/SKILL.md) Implement Phase 4 only for 001-quant-ops-dashboard.

Before coding, read spec.md, plan.md, data-model.md, contracts/*, quickstart.md, and tasks.md. Identify the exact task IDs for this phase and any prerequisites, then implement only that set.

Phase 4 scope:
- Implement the React web app using Hooks, TypeScript, Redux Toolkit, RTK Query, and React Router according to the plan.
- Wire the app shell, providers, store, route map, auth shell, and error boundaries.
- Implement the overview page.
- Implement strategy list and strategy detail pages.
- Implement decisions page with filtering, search, sort, deep linking, and detail drawer/page behavior.
- Implement trades/orders page with lifecycle detail and terminal result visibility.
- Implement skipped trades page with standardized skip taxonomy and reason visibility.
- Implement alerts list plus dedicated /alerts/:alertId page, with drawer behavior where specified.
- Implement live feed wiring for decisions, trades, alerts, and health events through the real API and SSE layer.
- Implement loading, empty, error, reconnecting, and degraded states.
- Implement UTC/local time toggle and deep-linkable state where required.

Do not implement admin control pages or full PnL analytics in this run unless a dependency absolutely requires a minimal shared component.

Validation required:
- web app builds cleanly
- route-level tests pass
- core operator journeys pass in component/integration/E2E coverage
- no page depends on mocked production data
```
