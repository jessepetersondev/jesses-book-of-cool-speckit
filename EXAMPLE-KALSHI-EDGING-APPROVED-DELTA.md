# Kalshi Edging Approved-Delta Sequence

Observed source: `/home/ai/.codex/history.jsonl`, session `019d7a23-845a-7eb0-a3d5-715a3b825d56`

Use this when the repo already exists, already went through Spec Kit, and you want the stricter minimal-diff brownfield workflow you used on `kalshi-edging-quant`.

Observed extra operator notes:

- `Create the quality.md file for this app before we do speckit implement.`
- the same `speckit-implement` prompt was sent multiple times

## 1. Constitution

```text
[$speckit-constitution](/home/ai/kalshi-edging-quant/.agents/skills/speckit-constitution/SKILL.md) Update the project constitution for an existing Spec Kit-managed application.

Context:
This repository already exists, has already gone through Spec Kit, and is being updated incrementally.

Primary repo:
- /home/ai/clawd/projects/kalshi-edging-quant

Related integration service:
- /home/ai/clawd/projects/kalshi-integration-event-publisher

Current update goal:
kalshi-edging-quant must stop directly submitting Kalshi execution/order actions in scope.
Instead, it must call kalshi-integration-event-publisher, which defines and performs the RabbitMQ publishing path.

Critical invariant:
All other functionality must remain exactly the same unless a change is absolutely required to complete the execution-path migration.

Update the constitution so future brownfield changes in this repo follow these principles:
- Treat this as an incremental update to an existing application, not a new build
- Preserve current implemented behavior unless an approved change explicitly modifies it
- Prefer the smallest possible safe diff
- Do not change a single line unless required by the approved delta
- Avoid unrelated refactors, cleanups, modernization, renames, and file churn
- For execution-path changes, keep responsibilities explicit:
  - kalshi-edging-quant = decisioning and execution intent generation
  - kalshi-integration-event-publisher = RabbitMQ publishing boundary
  - downstream consumer = actual execution
- Preserve all non-execution behavior exactly where practical
- Preserve observability and traceability wherever required
- Every update must define what changes and what must remain untouched
- Every task must have a verifiable completion condition
- When uncertain, choose the approach that touches fewer files and fewer lines
```

## 2. Specify

```text
[$speckit-specify](/home/ai/kalshi-edging-quant/.agents/skills/speckit-specify/SKILL.md) Update the existing specification for this Spec Kit-managed application to reflect a narrowly scoped change.

This is an update to an existing application, not a new application.
Use the current implemented system and existing approved artifacts as the baseline.
Do not redefine unrelated parts of the application.
Describe only the requested delta.

Primary repo:
- /home/ai/clawd/projects/kalshi-edging-quant

Related integration service:
- /home/ai/clawd/projects/kalshi-integration-event-publisher

Requested update:
kalshi-edging-quant should no longer directly execute or submit Kalshi order/execution actions in scope.
Instead, whenever it would currently submit an order or execution-related Kalshi action, it must call or use kalshi-integration-event-publisher so the message is placed onto RabbitMQ according to the publisher’s defined contract.

Baseline assumptions:
- The existing implemented behavior and prior approved artifacts are the source-of-truth baseline
- All current strategy logic, signal logic, scoring, scheduling, filtering, monitoring, reconciliation, storage behavior, and all non-execution functionality should remain exactly the same unless absolutely required for this update
- This update changes only the direct execution/order-submission path in scope

Update the specification to include:
1. Existing baseline behavior relevant to this change
2. Requested delta
3. Exact in-scope changes
4. Explicit out-of-scope changes
5. Service responsibility boundaries
6. Request flow from kalshi-edging-quant to kalshi-integration-event-publisher
7. Message publication expectations as defined by kalshi-integration-event-publisher
8. Execution handoff expectations for downstream consumers
9. Request/message contract requirements
10. Reliability requirements
11. Idempotency requirements
12. Retry/failure-handling requirements
13. Observability and traceability requirements
14. Rollout/migration constraints
15. User stories and operator stories with acceptance criteria
16. Risks
17. Assumptions
18. Open questions

Critical constraints:
- Preserve all existing behavior except the approved execution-path delta
- Do not broaden scope into redesign, cleanup, modernization, or unrelated architecture work
- Do not regenerate unrelated requirements
- Explicitly define what must remain identical
- Explicitly define which direct Kalshi execution/order-submission calls are in scope
- Explicitly define what modules and behaviors must remain untouched
- Do not jump into implementation details yet
```

## 3. Plan

```text
[$speckit-plan](/home/ai/kalshi-edging-quant/.agents/skills/speckit-plan/SKILL.md) Update the existing implementation plan for this Spec Kit-managed application to incorporate the approved change.

This is an incremental update to an existing application.
Use the current implementation and approved artifacts as the baseline.
Preserve prior architecture and implementation decisions unless this specific change requires modification.
Show only the incremental technical impact of this update.

Repos/services involved:
- /home/ai/clawd/projects/kalshi-edging-quant
- /home/ai/clawd/projects/kalshi-integration-event-publisher

Objective:
Replace direct Kalshi execution/order-submission calls in kalshi-edging-quant with the smallest possible change so that the required order/execution message is sent through kalshi-integration-event-publisher and published to RabbitMQ, while preserving all other existing behavior exactly.

Update the implementation plan to include:
1. Baseline current-state architecture relevant to this change
2. Incremental target-state change
3. Explicit responsibility boundaries
4. Exact execution/order-submission code paths to replace in kalshi-edging-quant
5. API/request boundary between kalshi-edging-quant and kalshi-integration-event-publisher
6. Request schema / contract design as required by the publisher
7. Correlation and idempotency design
8. Error-handling and retry design
9. Minimal file-change strategy for kalshi-edging-quant
10. Required publisher-side assumptions or changes only if actually needed
11. Logging, metrics, and traceability plan
12. Persistence/state-tracking implications if any
13. Rollout and migration strategy
14. Backward-compatibility or coexistence strategy if needed
15. Test and parity-validation strategy
16. Risk register
17. Explicit mapping from each user story to technical components

Planning constraints:
- Preserve existing edging strategy and decisioning logic exactly
- Move only the direct execution/order-submission trigger path out of kalshi-edging-quant
- Make the fewest possible code changes
- Change the fewest possible files
- Do not redesign unrelated systems
- Do not rewrite or re-plan unrelated application areas
- Keep contracts explicit and auditable
- Preserve observability from decision to publish handoff
- Explicitly call out untouched areas that must remain unchanged
- Where previous plan sections are still valid, retain them rather than regenerating them
```

## 4. Checklist

```text
[$speckit-checklist](/home/ai/clawd/projects/kalshi-edging-quant/.agents/skills/speckit-checklist/SKILL.md) Generate or update a migration quality checklist for this incremental brownfield change.

Scope:
- Primary repo: /home/ai/clawd/projects/kalshi-edging-quant
- Related service: /home/ai/clawd/projects/kalshi-integration-event-publisher

This is an update to an existing Spec Kit-managed application.
The checklist should validate only the approved delta and its impact on the existing system.

The checklist should verify:
- scope is strictly limited to replacing direct Kalshi execution/order-submission calls with publisher-mediated RabbitMQ handoff
- all non-execution functionality remains unchanged
- strategy logic remains unchanged
- scheduling remains unchanged
- scoring remains unchanged
- filtering remains unchanged
- monitoring remains unchanged
- reconciliation remains unchanged
- service boundaries are explicit
- the request/message contract is fully defined
- required metadata is preserved across the handoff
- idempotency has been addressed
- retries and publish-failure handling are explicit
- duplicate execution risk is controlled
- observability is sufficient from decision to publish handoff
- rollout and rollback considerations are credible
- tests are sufficient to prove parity except for the execution boundary change
- no hidden redesign, cleanup, or unrelated refactor has crept into the update plan
- incremental tasks remain aligned to the approved migration scope
- the implementation plan minimizes number of touched files and lines where practical
- the updated artifacts remain consistent with prior approved behavior outside the delta

Create a single general quality checklist if possible.
Name it quality.md if the template allows.
```

## 5. Tasks

```text
[$speckit-tasks](/home/ai/kalshi-edging-quant/.agents/skills/speckit-tasks/SKILL.md) Generate only the incremental implementation tasks needed for this approved update.

This is an update to an existing Spec Kit-managed application.
Use the current implementation and approved artifacts as the baseline.
Do not regenerate unrelated implementation work.
Describe only the tasks needed for this specific delta.

Repos/services involved:
- /home/ai/clawd/projects/kalshi-edging-quant
- /home/ai/clawd/projects/kalshi-integration-event-publisher

Task requirements:
- Organize tasks by migration objective and user/operator story
- Separate tasks by repository/service
- Include exact file paths where practical
- Keep tasks granular enough for safe AI implementation
- Include inspection tasks to locate all direct Kalshi execution/order-submission paths in kalshi-edging-quant
- Include request-contract tasks between kalshi-edging-quant and kalshi-integration-event-publisher
- Include only the minimal producer/client changes in kalshi-edging-quant
- Include publisher-side implementation/update tasks only if actually required
- Include validation and test tasks
- Include parity-validation tasks proving all non-execution behavior remains unchanged
- Include migration/cutover tasks only if needed
- Mark safe parallel tasks
- Ensure every task has a verifiable completion condition
- Ensure no task exists without a story or plan justification

Preferred task flow:
1. inspect and catalog current direct Kalshi execution/order-submission points in kalshi-edging-quant
2. define the exact request contract and required metadata
3. replace only the direct execution/order-submission call sites with calls to kalshi-integration-event-publisher
4. implement or verify publisher behavior required to place the message on RabbitMQ
5. preserve tracing, logging, and failure handling only where required by the migration
6. add/update tests and validation checks
7. verify no unintended behavioral drift outside the execution boundary
8. prepare rollout/cutover steps only if necessary

Critical task-generation rule:
Prefer fewer files and fewer changed lines whenever possible.
Do not regenerate unrelated historical tasks from the existing app.
```

## 6. Analyze

```text
[$speckit-analyze](/home/ai/kalshi-edging-quant/.agents/skills/speckit-analyze/SKILL.md) Analyze the updated spec.md, plan.md, tasks.md, and quality checklist for this incremental brownfield change.

This is an update to an existing Spec Kit-managed application.
Compare the approved delta against the existing baseline behavior and existing approved artifacts.
Look for scope creep, contradictions, and unnecessary churn.

Find:
- contradictions between current-state and target-state assumptions
- any scope creep beyond direct Kalshi execution/order-submission rerouting
- service-boundary ambiguity
- missing incremental task coverage
- tasks with no story or plan justification
- weak contract definitions
- weak idempotency or retry coverage
- missing observability coverage
- missing parity-validation coverage
- plan elements that would unintentionally change behavior outside the execution boundary
- unnecessary refactors
- unnecessary file touches
- places where fewer changes could achieve the same migration result
- conflicts between prior approved artifacts and the new update

Produce an alignment report with exact edits needed before implementation begins.

Be especially strict about identifying anything that would violate:
- do not change a single line unless required for the RabbitMQ handoff
- all other functionality remains the exact same
- existing approved behavior is the baseline
```

## 7. Implement

```text
[$speckit-implement](/home/ai/kalshi-edging-quant/.agents/skills/speckit-implement/SKILL.md) Implement only the approved delta for this existing Spec Kit-managed application, using the updated spec.md, plan.md, tasks.md, and quality checklist.

Context:
This is an incremental update to an existing Kalshi quant application.

Repos/services involved:
- /home/ai/clawd/projects/kalshi-edging-quant
- /home/ai/clawd/projects/kalshi-integration-event-publisher

Required target flow:
- kalshi-edging-quant must stop directly submitting Kalshi execution/order actions in the migrated paths
- kalshi-edging-quant must instead call kalshi-integration-event-publisher
- kalshi-integration-event-publisher defines and performs the RabbitMQ publication path
- all other existing functionality in kalshi-edging-quant must remain exactly the same unless the updated approved artifacts explicitly require otherwise

Implementation rules:
- Use the current implementation as the baseline
- Implement only the approved delta
- Do not redesign strategy logic, signal logic, scoring, filtering, scheduling, reconciliation, monitoring, storage, or unrelated app behavior in kalshi-edging-quant
- Limit scope strictly to rerouting the direct execution/order-submission path
- Treat this as an incremental migration, not a rewrite
- Preserve current behavior exactly as much as possible except for the direct-execution responsibility change
- Do not add unrelated features, refactors, cleanups, renames, reorganizations, or file churn
- Change the fewest possible lines in the fewest possible files
- Keep responsibilities explicit:
  - kalshi-edging-quant = decisioning and execution intent generation
  - kalshi-integration-event-publisher = RabbitMQ publishing boundary
  - downstream consumer = execution
- Keep request/message contracts explicit, traceable, and auditable
- Preserve or improve logging, correlation IDs, idempotency protections, retries, and failure visibility only where required by the approved artifacts
- Follow incremental tasks.md work in dependency order
- Respect any cutover and validation requirements defined in the approved artifacts

Execution expectations:
1. Identify all direct Kalshi execution/order-submission paths in kalshi-edging-quant that are in scope
2. Replace only those direct execution/order-submission paths with the approved call pattern into kalshi-integration-event-publisher
3. Implement or verify the publisher-side request-to-RabbitMQ behavior as defined by the approved contracts
4. Preserve observability and error handling required by the approved artifacts
5. Add or update only the tests and validation steps required by the approved update
6. Keep changes minimal, targeted, and production-oriented

While implementing:
- Reuse existing code paths and abstractions where practical
- Prefer minimal safe diffs over broad refactors
- If a contract or boundary is underspecified, consult the updated spec.md and plan.md first
- If still ambiguous, stop and surface the exact ambiguity instead of inventing new scope
- Explicitly avoid touching files not required for the migration
- Do not re-implement previously completed unrelated tasks

After each major checkpoint:
- report what changed
- report which repo/service changed
- report what was validated
- report any remaining tasks
- report any blocker or mismatch discovered between implementation reality and the approved artifacts

Definition of done:
- kalshi-edging-quant no longer directly submits Kalshi execution/order actions in the migrated paths
- kalshi-edging-quant calls kalshi-integration-event-publisher instead
- the publisher places the required message onto RabbitMQ as defined
- required tests and validation checks for this update pass
- no unintended behavior drift was introduced outside the execution-path change
- the implementation matches the updated spec.md, plan.md, tasks.md, and quality checklist
```
