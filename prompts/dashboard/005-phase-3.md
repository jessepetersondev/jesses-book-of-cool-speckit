# Kalshi Quant Dashboard Phase 3 Prompt

Observed source: `/home/ai/.codex/history.jsonl`, session `019d7c0f-6eff-7920-85ac-aab67a3bc180`

```text
[$speckit-implement](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-implement/SKILL.md) Implement Phase 3 only for 001-quant-ops-dashboard.

Before coding, read spec.md, plan.md, data-model.md, contracts/*, quickstart.md, and tasks.md. Identify the exact task IDs for this phase and any prerequisites, then implement only that set.

Phase 3 scope:
- Implement authentication and session handling as planned.
- Implement effective capability resolution from role bindings plus access/export policy.
- Implement the shared capability/session contract surface, including allowedExportResources or the equivalent source of truth used by both UI gating and backend enforcement.
- Implement RBAC enforcement for operator, developer, and admin across raw payload access, exports, admin surfaces, detail endpoints, and live subscriptions.
- Implement REST APIs for overview, strategies, decisions, trades, skips, alerts list, alert detail, and the read-side surfaces needed by the UI.
- Implement the live update channel using the planned SSE path at apps/api/src/plugins/sse.ts, with role-aware subscription filtering or denial where required.
- Implement export endpoint behavior and authorization enforcement where those tasks are in scope.
- Keep OpenAPI/contracts, handlers, schemas, and docs synchronized.

Do not implement the full visual UI layer in this run.

Validation required:
- contract tests pass for REST and live-update surfaces
- negative authorization tests pass
- alert detail is reachable through a dedicated detail endpoint supporting /alerts/:alertId
- SSE authorization behavior is covered by integration tests
```
