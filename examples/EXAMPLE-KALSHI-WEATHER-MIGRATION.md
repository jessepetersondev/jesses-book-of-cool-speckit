# Kalshi Weather Quant Migration Sequence

Observed source: `/home/ai/.codex/history.jsonl`, session `019d583d-07b2-7a23-989d-51b1c48a1792`

Use this when you want the multi-repo migration pattern that moved direct execution out of `kalshi-weather-quant` and through the publisher plus RabbitMQ boundary.

Back to [KALSHI-EXAMPLES.md](KALSHI-EXAMPLES.md)

Workflow family:

- [FRAMEWORK-BROWNFIELD-APPROVED-DELTA-TEMPLATE.md](../templates/FRAMEWORK-BROWNFIELD-APPROVED-DELTA-TEMPLATE.md) as the base brownfield control model

Use this example when:

- the change spans multiple repos
- one repo becomes a boundary or handoff point for another
- you need `clarify` before `plan` because the contract and responsibility split is still ambiguous

How to read this file:

1. start from the brownfield template for the control model
2. use this file for the extra cross-repo `specify`, `clarify`, and `plan` language
3. preserve explicit service-boundary ownership throughout the migration

## 1. Specify

```text
[$speckit-specify](/home/ai/clawd/projects/kalshi-weather-quant/.agents/skills/speckit-specify/SKILL.md) Create a baseline change specification for an existing multi-repo Kalshi architecture migration.

Primary repo:
- /home/ai/clawd/projects/kalshi-weather-quant

Related repos:
- /home/ai/clawd/projects/kalshi-integration-event-publisher
- /home/ai/clawd/projects/kalshi-integration-executor

Requested change:
kalshi-weather-quant should no longer execute Kalshi actions directly.
Instead, for all action attempts into Kalshi, it should call kalshi-integration-event-publisher.
kalshi-integration-event-publisher will publish the appropriate command message into RabbitMQ.
kalshi-integration-executor is already listening and will execute those actions from RabbitMQ messages.

Goal:
Refactor the architecture so weather-quant remains responsible for decisioning and action intent generation, event-publisher becomes the publishing boundary into RabbitMQ, and executor remains the action execution service.

The specification must describe this as a migration of an existing system, not a new app.

The spec must include:
1. Business/engineering objective
2. Existing behavior summary
3. Desired target behavior
4. In-scope changes
5. Explicit out-of-scope changes
6. Service boundary definitions for all three repos
7. Request flow from weather-quant to event-publisher
8. RabbitMQ publish flow from event-publisher
9. Executor consumption/execution flow
10. Command message requirements
11. Reliability requirements
12. Idempotency requirements
13. Retry/failure-handling requirements
14. Observability and traceability requirements
15. Rollout/migration constraints
16. User stories and operator stories with acceptance criteria
17. Risks
18. Assumptions
19. Open questions

Important constraints:
- Preserve current weather-quant strategy and signal logic unless explicitly required to change
- Focus on rerouting execution responsibility, not redesigning the product
- weather-quant should stop performing direct Kalshi execution and instead call event-publisher
- event-publisher should own publishing messages into RabbitMQ
- executor should continue owning execution of actions from RabbitMQ
- Do not jump into implementation details yet
```

## 2. Clarify

```text
[$speckit-clarify](/home/ai/clawd/projects/kalshi-weather-quant/.agents/skills/speckit-clarify/SKILL.md) Interrogate the migration spec for ambiguity and missing architecture decisions.

Focus especially on clarifying:
- What exact Kalshi actions are currently performed directly in kalshi-weather-quant
- Which of those actions must now become calls to kalshi-integration-event-publisher
- What request contract weather-quant sends to event-publisher
- What RabbitMQ message contract event-publisher publishes
- Whether event-publisher performs transformation or validation before publish
- How executor acknowledges success/failure
- Whether execution results return via RabbitMQ, API callback, events, database, or logs
- Which repository owns the command schema
- How retries behave between weather-quant and event-publisher
- How retries behave between event-publisher and RabbitMQ
- How duplicate execution is prevented
- How rollback/coexistence should work during migration
- Whether feature flags or phased cutover are required
- What operational dashboards and logs are required
- What acceptance tests are needed across repo boundaries

Update the spec so ambiguity is minimized before technical planning.
Do not proceed while major responsibility or contract ambiguity remains.
```

## 3. Plan

```text
[$speckit-plan](/home/ai/clawd/projects/kalshi-weather-quant/.agents/skills/speckit-plan/SKILL.md) Create the technical implementation plan for this architectural migration based on the approved spec.

Repos involved:
- /home/ai/clawd/projects/kalshi-weather-quant
- /home/ai/clawd/projects/kalshi-integration-event-publisher
- /home/ai/clawd/projects/kalshi-integration-executor

Objective:
Replace direct Kalshi execution in kalshi-weather-quant with calls to kalshi-integration-event-publisher, which publishes RabbitMQ command messages that are consumed and executed by kalshi-integration-executor.

The plan must include:
1. Current-state architecture summary
2. Target-state architecture
3. Clear responsibility boundaries
4. API/request boundary between weather-quant and event-publisher
5. RabbitMQ publish topology owned by event-publisher
6. Queue/exchange/routing-key strategy
7. Command message schema design
8. Correlation and idempotency design
9. Producer-client changes required in weather-quant
10. Publish-path changes required in integration-event-publisher
11. Consumer/execution expectations in integration-executor
12. Error-handling and retry design
13. Dead-letter and poison-message handling
14. Persistence/state-tracking implications
15. Logging and observability plan
16. Rollout and migration strategy
17. Backward-compatibility or coexistence strategy
18. Test strategy across repo boundaries
19. Risk register
20. Explicit mapping from each user story to technical components and repos

Technical principles:
- Preserve current trading/decision logic in weather-quant
- Move only the execution trigger path out of weather-quant
- event-publisher owns RabbitMQ publishing
- executor owns execution
- Minimize behavioral drift
- Keep contracts explicit and versionable
- Design for auditability and traceability
- Do not introduce unrelated architecture changes
```

## 4. Tasks

```text
[$speckit-tasks](/home/ai/clawd/projects/kalshi-weather-quant/.agents/skills/speckit-tasks/SKILL.md) Generate actionable implementation tasks from the approved migration spec and plan.

Repos involved:
- /home/ai/clawd/projects/kalshi-weather-quant
- /home/ai/clawd/projects/kalshi-integration-event-publisher
- /home/ai/clawd/projects/kalshi-integration-executor

Task requirements:
- Organize tasks by migration objective and user/operator story
- Separate tasks by repository
- Include exact file paths where practical
- Keep tasks granular enough for safe AI implementation
- Include request-contract tasks between weather-quant and event-publisher
- Include publish-path tasks for integration-event-publisher
- Include executor verification/alignment tasks for integration-executor
- Include validation and test tasks
- Include migration/cutover tasks
- Mark safe parallel tasks
- Ensure every task has a verifiable completion condition

Preferred task flow:
1. inspect current direct execution points in weather-quant
2. define shared request/message contracts
3. replace direct execution calls in weather-quant with calls to event-publisher
4. implement or update event-publisher publish flow into RabbitMQ
5. verify executor compatibility with the published messages
6. add observability and tracing across all repos
7. add integration and failure-path tests
8. prepare migration/cutover steps
```

## 5. Implement

```text
[$speckit-implement](/home/ai/clawd/projects/kalshi-weather-quant/.agents/skills/speckit-implement/SKILL.md) Implement this migration strictly from the approved spec.md, plan.md, tasks.md, and quality checklist.

Context:
This is an existing multi-repo Kalshi architecture migration.

Repos involved:
- /home/ai/clawd/projects/kalshi-weather-quant
- /home/ai/clawd/projects/kalshi-integration-event-publisher
- /home/ai/clawd/projects/kalshi-integration-executor

Required target flow:
- kalshi-weather-quant must stop executing Kalshi actions directly
- kalshi-weather-quant must instead call kalshi-integration-event-publisher
- kalshi-integration-event-publisher must publish the appropriate action message into RabbitMQ
- kalshi-integration-executor is already listening and must execute those actions from RabbitMQ

Implementation rules:
- Do not redesign the strategy logic, signal logic, scoring, or market-selection logic in kalshi-weather-quant unless the approved spec explicitly requires it
- Limit scope to rerouting the execution path
- Treat this as a migration, not a rewrite
- Preserve existing behavior as much as possible except for the direct-execution responsibility change
- Do not add unrelated platform features or refactors
- Keep service responsibilities explicit:
  - weather-quant = decisioning and action intent generation
  - integration-event-publisher = publish boundary into RabbitMQ
  - integration-executor = execution consumer
- Keep message/request contracts explicit, traceable, and auditable
- Preserve or improve logging, correlation IDs, idempotency handling, retries, and failure visibility where required by the approved artifacts
- Follow tasks.md in dependency order
- Respect any repo boundaries, cutover steps, and validation requirements defined in the approved artifacts

Execution expectations:
1. Inspect the current implementation and identify all direct Kalshi execution paths in kalshi-weather-quant
2. Replace those direct execution paths with the approved call pattern into kalshi-integration-event-publisher
3. Implement or update the publisher-side request-to-RabbitMQ flow in kalshi-integration-event-publisher as defined in the approved contracts
4. Verify and adjust integration compatibility with kalshi-integration-executor only as required by the approved plan
5. Implement observability, tracing, and failure handling required by the approved artifacts
6. Add or update tests and validation steps required by tasks.md
7. Keep changes minimal, targeted, and production-oriented

While implementing:
- Reuse existing code paths and abstractions where practical
- Prefer minimal safe diffs over broad refactors
- If a contract or responsibility boundary is underspecified, consult spec.md and plan.md first
- If still ambiguous, stop and surface the exact ambiguity instead of inventing new scope
- Update the relevant repo artifacts only where necessary to complete the approved migration

After each major checkpoint:
- report what changed
- report which repo changed
- report what was validated
- report any remaining tasks
- report any blocker or mismatch discovered between implementation reality and the approved artifacts

Definition of done:
- kalshi-weather-quant no longer directly executes Kalshi actions in the migrated paths
- weather-quant calls integration-event-publisher instead
- integration-event-publisher publishes the approved action messages into RabbitMQ
- integration-executor can consume and execute those actions as expected
- logging and traceability are sufficient to follow an action from decision to publish to execution
- required tests and validation checks pass
- the implementation matches the approved spec.md, plan.md, tasks.md, and quality checklist
```

## Note

No customized constitution or checklist prompt was recovered in this same session. For the stricter brownfield-safe pattern that adds those controls, use `kalshi-edging-approved-delta-sequence.md`.
