# Plan Highlights

Source:

- `/home/ai/clawd/projects/kalshi-quant-dashboard/specs/001-quant-ops-dashboard/plan.md`

## Why This Plan Is A Good Reproduction Target

- it has a strong technical-context section
- it re-checks the constitution before implementation
- it defines the exact source tree
- it names the design-output files, not just the app architecture
- it makes route state, SSE, auth, mixed ingestion, and deployment readiness explicit

## Sections That Matter Most

1. Summary
   The plan states the real product shape in one paragraph.

2. Technical Context
   What good looks like:
   - language and runtime
   - dependencies
   - storage
   - testing
   - target platform
   - auth/RBAC
   - contracts
   - observability
   - performance goals
   - constraints

3. Constitution Check
   This is the explicit pass/fail gate before implementation.

4. Project Structure
   The source tree is concrete enough that tasks can point at real file paths.

5. Phase 1 Design Outputs
   The plan names the artifacts that must exist before coding:
   - `data-model.md`
   - `contracts/rest-api.openapi.yaml`
   - `contracts/live-updates.yaml`
   - `contracts/normalized-events.md`
   - `contracts/source-compatibility.md`
   - `contracts/rbac-matrix.md`
   - `contracts/session-capabilities.md`
   - `quickstart.md`

6. Route Map and State Management
   The plan defines the real route surface and deep-link behavior before the UI is implemented.

## Reproduction Bar

- make the source tree concrete
- name the required design outputs
- define auth, contracts, SSE, and observability before coding
- keep the plan aligned with the actual intended file layout
