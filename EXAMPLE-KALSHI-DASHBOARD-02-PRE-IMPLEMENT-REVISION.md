# Kalshi Quant Dashboard Revision Sequence

Observed source: `/home/ai/.codex/history.jsonl`, session `019d7c0f-6eff-7920-85ac-aab67a3bc180`

This is the exact revision pass that happened before the phased `speckit-implement` runs.

Back to [KALSHI-EXAMPLES.md](KALSHI-EXAMPLES.md)

Workflow this example follows:

- [FRAMEWORK-PHASED-MULTI-IMPLEMENT-TEMPLATE.md](FRAMEWORK-PHASED-MULTI-IMPLEMENT-TEMPLATE.md)

Dashboard read order:

1. [01 Initial Build](EXAMPLE-KALSHI-DASHBOARD-01-INITIAL-BUILD.md)
2. `02 Pre-Implement Revision` <- you are here
3. [03 Strict Phased Mode](EXAMPLE-KALSHI-DASHBOARD-03-STRICT-PHASED-MODE.md)
4. [04 Phase 2 Prompt](EXAMPLE-KALSHI-DASHBOARD-04-PHASE-2.md)
5. [05 Phase 3 Prompt](EXAMPLE-KALSHI-DASHBOARD-05-PHASE-3.md)
6. [06 Phase 4 Prompt](EXAMPLE-KALSHI-DASHBOARD-06-PHASE-4.md)

What this file captures:

- the `analyze -> revise spec -> revise plan -> regenerate tasks -> analyze again` gate
- the artifact-stabilization work that happens before phased implementation begins

Previous file:

- [EXAMPLE-KALSHI-DASHBOARD-01-INITIAL-BUILD.md](EXAMPLE-KALSHI-DASHBOARD-01-INITIAL-BUILD.md)

Next file:

- [EXAMPLE-KALSHI-DASHBOARD-03-STRICT-PHASED-MODE.md](EXAMPLE-KALSHI-DASHBOARD-03-STRICT-PHASED-MODE.md)

## 1. Analyze Hidden Assumptions

```text
[$speckit-analyze](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-analyze/SKILL.md) Focus on hidden assumptions around upstream event schemas, idempotent ingestion, skipped-trade coverage, PnL correctness, live/historical convergence, RabbitMQ operational coverage, auth/RBAC, and deployment readiness. Flag any missing contracts, data models, or test scenarios before implementation.
```

## 2. Revise Spec

```text
[$speckit-specify](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-specify/SKILL.md) Revise the active 001-quant-ops-dashboard spec to fully preserve and clarify the remaining admin security/control surface. Do not narrow FR-002c, FR-002e, or FR-002f.

Required spec corrections:
- Make admin-managed access policy and export-scope policy first-class product features, not implied behavior from role_binding or a boolean raw-export flag.
- Explicitly require a contract-backed source of truth for effective capabilities and allowed export resources/scopes so both UI gating and backend enforcement use the same policy result.
- Add an admin surface for access/export policy management at /admin/access-policies, including viewing, creating, updating, and auditing policy changes.
- Keep role differences explicit for operator vs developer vs admin across:
  - raw payload visibility
  - export permissions and export scope
  - live subscriptions
  - admin configuration surfaces
  - audit-log visibility where applicable
- Make feature-flag administration fully round-trip at the product level: admins can view current flag state, update flags, see validation errors, and audit who changed what and when.
- Preserve audit logging requirements for all admin mutations, including access policy changes, export policy changes, and feature-flag updates.
- Do not change unrelated product scope unless needed to remove ambiguity.

Regenerate spec.md so the admin control surface is explicit, internally consistent, and still production-ready.
```

## 3. Revise Plan

```text
[$speckit-plan](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-plan/SKILL.md) Revise the technical plan and derived design artifacts for the active 001-quant-ops-dashboard feature to fully close the remaining analyze findings around admin policy control, feature-flag mutation contracts, and plan/task file-layout drift.

Regenerate and align at minimum:
- plan.md
- data-model.md
- contracts/rest-api.openapi.yaml
- contracts/rbac-matrix.md
- any session/effective-capabilities contract artifacts
- quickstart.md if admin setup or permissions flows change

Mandatory design fixes:

1. Access/export policy model (G1)
- Add explicit entities and contracts for:
  - access_policy
  - access_policy_rule or equivalent rule/grant model
  - export_scope / allowed_export_resource model or equivalent source of truth
  - effective_capability resolution per user/session
  - audit log records for policy mutations
- Keep role_binding, but stop treating it as the sole authorization model.
- Define how effective capabilities are resolved from roles plus policy.
- Define how allowedExportResources is represented in shared contracts and surfaced to both API enforcement and frontend UI gating.
- Add admin page/route design for /admin/access-policies.
- Add REST design for read/write admin policy management, including validation, conflict handling, denial responses, and audit-log behavior.
- Cover policy effects on exports, raw payload visibility, live subscriptions, and admin-only surfaces.

2. Feature-flag write-side contract (G2)
- Add explicit write contracts for feature-flag mutation, such as PATCH or PUT endpoints, request/response schemas, validation errors, denial responses, optimistic concurrency/versioning if used, and audit-log behavior.
- Add admin page behavior for viewing and updating feature flags.
- Define automated verification scenarios for successful updates, denied updates, invalid payloads, and audit-log creation.

3. Verification design
- Add contract/integration/E2E validation for:
  - effective capability resolution per role and policy
  - allowedExportResources returned correctly
  - export denial for unauthorized resources
  - raw payload access differences by role/policy
  - admin-only access to policy and feature-flag mutation endpoints/pages
  - SSE/live-subscription denial or filtering where role/policy requires it
  - audit-log creation for all admin mutations

4. File-layout consistency cleanup (I1)
- Update the plan’s source-tree sketch so it matches the intended task/file paths:
  - SSE implementation lives at apps/api/src/plugins/sse.ts
  - schema docs live under docs/schema/*
- Remove or rename conflicting structure references such as apps/api/src/streams/ if that is not the intended path.

Output requirements:
- Do not reduce scope to "boolean flag only" authorization.
- Keep the design contract-first and implementation-ready.
- Ensure the admin control surface is fully represented across data model, page map, API contracts, and verification strategy.
```

## 4. Regenerate Tasks

```text
[$speckit-tasks](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-tasks/SKILL.md) Regenerate tasks.md from the revised spec and plan. Close all remaining partial coverage for FR-002c, FR-002e, and FR-002f, and remove the current mismatch between plan layout and task paths.

Required task coverage:

1. Access/export policy implementation
- Add concrete tasks for schema/model/migration work covering access_policy, policy rules, allowed export resources/scopes, effective capability resolution, and audit logging.
- Add backend tasks for policy evaluation and enforcement on:
  - exports
  - raw payload access
  - admin pages/endpoints
  - live subscriptions/SSE filtering or denial
- Add frontend/admin tasks for /admin/access-policies including list, detail, edit/create flows, error states, and audit visibility where required.
- Add shared contract tasks for allowedExportResources and effective capabilities.

2. Feature-flag administration
- Add tasks for write-side REST/OpenAPI contracts for feature-flag mutation.
- Add backend tasks for update handling, validation, authorization, persistence, and audit logs.
- Add frontend/admin tasks for feature-flag editing UI.
- Add automated tests for:
  - successful update
  - denied update
  - invalid payload
  - audit-log generation

3. Verification tasks
- Add contract, integration, and E2E tests for:
  - role/policy capability differences
  - export-scope enforcement
  - raw payload visibility differences
  - admin-only page/API access
  - SSE/live-subscription authorization behavior
  - allowedExportResources returned correctly in session/effective-capability responses

4. File-layout alignment
- Add cleanup/update tasks so plan.md, tasks.md, and implementation paths all agree on:
  - apps/api/src/plugins/sse.ts
  - docs/schema/*

Task generation rules:
- Include exact file paths.
- Include dependencies.
- Include verification criteria for every task.
- Mark safe parallel tasks with [P].
- Ensure no task assumes admin update behavior that the contracts still do not define.
```

## 5. Re-Analyze Remaining Issues

```text
[$speckit-analyze](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-analyze/SKILL.md) Re-run analysis with emphasis on the remaining prior issues only:

- G1: admin access/export policy model, route/API coverage, effective capability contract, and allowedExportResources source of truth
- G2: feature-flag write-side contract coverage plus automated verification for update, denial, and audit logging
- I1: plan/task file-layout consistency, especially apps/api/src/plugins/sse.ts and docs/schema/*

Also verify:
- FR-002c, FR-002e, and FR-002f are no longer only partially covered
- the RBAC/session contracts and OpenAPI are aligned
- no task assumes admin update behavior that the contracts do not define
- no new contradictions were introduced while expanding the admin control surface
```
