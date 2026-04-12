# Before And After Analyze

This is the clearest repair-loop example in the repo.

Use it to understand why the dashboard workflow did not jump from the first artifact pass straight into `speckit-implement`.

## The Sequence

```mermaid
flowchart LR
    A[Initial Build Pack] --> B[Artifacts Exist But Are Not Safe Yet]
    B --> C[Analyze Hidden Assumptions]
    C --> D[Revise Spec]
    D --> E[Revise Plan]
    E --> F[Regenerate Tasks]
    F --> G[Re-Analyze]
    G --> H[Enable Strict Phased Mode]
```

Reference packs:

- [generated-initial-build-pack.md](generated-initial-build-pack.md)
- [generated-pre-implement-revision-pack.md](generated-pre-implement-revision-pack.md)
- [generated-strict-phased-mode-pack.md](generated-strict-phased-mode-pack.md)

## What Was Wrong Before Analyze

The initial build pass produced a large, serious dashboard specification and plan, but the later revision prompts show three concrete risks still existed:

| Area | What was still weak before analyze | Why it was risky |
|---|---|---|
| Admin policy model | Access policy and export scope were not yet explicit first-class product surfaces. | UI gating and backend enforcement could have drifted apart. |
| Feature-flag control | Feature-flag administration was not yet fully round-trip and contract-backed. | Admin pages could exist without truthful mutation contracts, validation, or audit behavior. |
| Plan or task file layout | The intended SSE and schema-doc paths were not fully aligned. | Tasks could point at the wrong tree, leading to churn and fake completion. |

That is why the repair prompt targeted `FR-002c`, `FR-002e`, and `FR-002f` instead of starting implementation immediately.

## What Changed In `spec.md`

The revised spec made the admin control surface explicit instead of implied.

Concrete evidence from the real dashboard artifact:

- The clarification section now states that access policy, export-scope policy, and feature-flag administration are first-class product features with a contract-backed effective-capability result and a dedicated `/admin/access-policies` surface.
- The spec defines explicit role differences for operator, developer, and admin across raw payload visibility, export scope, live subscription visibility, and admin controls.
- `FR-002c`, `FR-002e`, and `FR-002f` now explicitly require export-scope policy, admin control surfaces, and capability enforcement across exports, raw payloads, live subscriptions, and admin pages.

Why that matters:

- the product contract became testable
- admin behavior stopped being hidden inside implementation assumptions
- later API and UI tasks had a truthful product source of truth

See:

- [SPEC-HIGHLIGHTS.md](SPEC-HIGHLIGHTS.md)

## What Changed In `plan.md`

The revised plan turned the new product requirements into concrete design surfaces.

Concrete evidence from the real dashboard artifact:

- the technical context now resolves authorization as `role_binding + access_policy + export_scope` into one effective capability result
- the project structure explicitly says SSE lives at `apps/api/src/plugins/sse.ts`
- schema documentation is explicitly located under `docs/schema/`
- the route map includes `/admin/access-policies` and `/admin/feature-flags`
- the API design includes read and write endpoints for access-policy and feature-flag administration
- the plan defines `allowedExportResources` as a shared source of truth used by both enforcement and UI gating

Why that matters:

- the task file can point at real paths
- OpenAPI, runtime schemas, and frontend contracts have a shared design target
- phased implementation can split backend enforcement from UI work without losing alignment

See:

- [PLAN-HIGHLIGHTS.md](PLAN-HIGHLIGHTS.md)

## What Changed In `tasks.md`

The revised task set closed the exact analyze gaps with explicit build and verification work.

Concrete evidence from the real dashboard artifact:

- tasks were added for shared admin contracts, access-policy schema, effective-capability schema, and feature-flag schema
- tasks were added for admin API routes, admin pages, and mutation wiring
- tests were added for capability resolution, `allowedExportResources`, raw-payload visibility, feature-flag mutation success or denial, and SSE authorization behavior
- file-layout alignment tasks explicitly verified `apps/api/src/plugins/sse.ts` and `docs/schema/*`
- the traceability section at the bottom now maps build and verification tasks directly to `FR-002c`, `FR-002e`, and `FR-002f`

Why that matters:

- the repair loop did not stop at prose
- the verification burden moved into the task graph
- later implementation prompts could stay narrow because the task ordering already carried the dependency structure

See:

- [TASKS-HIGHLIGHTS.md](TASKS-HIGHLIGHTS.md)

## Why Strict Phased Mode Came Next

After the repair loop, the artifacts were stronger, but the feature was still too large for one safe build pass.

The real task set had to cover:

- mixed-source ingestion and normalization
- auth and capability enforcement
- SSE and REST surfaces
- operator UI
- admin policy and feature-flag surfaces
- docs, runbooks, and release readiness

One `speckit-implement` run would have mixed too many layers. Strict phased mode came next because it let the workflow:

- isolate ingestion and persistence before UI
- isolate auth, contracts, and SSE before the main React surface
- validate each slice before continuing

That is why the next preserved step is not “implement everything.” It is the phased-mode lock followed by separate phase prompts.

## Reproduction Rule

If your first pass leaves policy, contracts, path layout, or verification ambiguous, do not start coding.

Run:

```text
analyze -> revise spec -> revise plan -> regenerate tasks -> analyze again
```

Then decide whether one `implement` pass is still safe. If not, switch to phased mode before code starts.
