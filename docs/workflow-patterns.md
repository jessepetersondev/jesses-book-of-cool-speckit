# Workflow Patterns

These are the reusable SpecKit workflow patterns derived from real usage.

## 1. Greenfield Build

Use this when:

- the product is new
- there is no meaningful implementation baseline
- you want the full product-definition flow before implementation

Command pattern:

1. `speckit-constitution`
2. `speckit-specify`
3. `speckit-clarify`
4. `speckit-plan`
5. `speckit-checklist`
6. `speckit-tasks`
7. `speckit-analyze`
8. `speckit-implement`

Best for:

- SaaS MVPs
- internal tools
- new monorepos
- new products where scope clarity matters more than preserving an existing baseline

Framework rule:

- the prompt body should constrain scope tightly
- the spec should define product boundaries before implementation begins

Kalshi example:

- `kalshi-edge-saas`

## 2. Brownfield Approved-Delta Update

Use this when:

- the application already exists
- behavior must stay stable outside one requested change
- you want SpecKit without inviting a rewrite

Command pattern:

1. `speckit-constitution` or constitution update
2. `speckit-specify` for the requested delta only
3. `speckit-plan` for the incremental technical impact only
4. `speckit-checklist` for migration quality and parity
5. `speckit-tasks` for delta-only work
6. `speckit-analyze` for scope creep and drift
7. `speckit-implement` with strict minimal-diff language

Best for:

- migrations
- integrations
- boundary changes
- preserving production behavior while changing one narrow subsystem

Framework rule:

- explicitly define unchanged behavior
- force minimal changed files and minimal changed lines
- do not let task generation broaden the project

Kalshi examples:

- `kalshi-weather-quant`
- `kalshi-edging-quant`

## 3. Phased Multi-Implement Build

Use this when:

- the feature is large
- one implement pass is too broad
- you need multiple build stages with hard stop points

Command pattern:

1. initial spec and plan generation
2. `speckit-analyze`
3. revise `spec.md`
4. revise `plan.md`
5. regenerate `tasks.md`
6. re-run `speckit-analyze`
7. set strict phased mode
8. run multiple scoped `speckit-implement` passes

Typical implement pass naming:

- `Implement Phase 2 only`
- `Implement Phase 3 only`
- `Implement Phase 4 only`

Best for:

- control planes
- dashboards
- multi-package systems
- ingestion plus backend plus UI builds

Framework rule:

- each implement pass should be dependency-closed
- each pass should end with validation and the next recommended phase
- later phases must not leak into the current run

Kalshi example:

- `kalshi-quant-dashboard`

## Practical Rule Set

The reusable command structure is:

- start with the stock SpecKit skills
- wrap them with a strong prompt body
- re-run planning artifacts when analyze shows gaps
- use single-pass implementation for narrow work
- use phased implementation for large work
- use brownfield-safe prompts when preserving an existing system matters
