# Phase Split

This is the important implementation split from the real dashboard workflow.

## Why The Split Matters

The dashboard was too large for one safe `speckit-implement` run.

The phase boundaries reduced:

- scope leakage
- file churn
- validation noise
- cross-layer regression risk

## Preserved Phase Map

| Phase | Primary focus | Validation emphasis |
|---|---|---|
| Phase 2 | ingestion, normalization, persistence, replay safety | migrations, ingestion integration tests, replay/redelivery behavior |
| Phase 3 | auth, capabilities, API, SSE, enforcement | contract tests, authorization tests, SSE enforcement |
| Phase 4 | operator-facing React UI | route-level tests, operator journeys, real API wiring |

## Reference Prompts

- [../../EXAMPLE-KALSHI-DASHBOARD-04-PHASE-2.md](../../EXAMPLE-KALSHI-DASHBOARD-04-PHASE-2.md)
- [../../EXAMPLE-KALSHI-DASHBOARD-05-PHASE-3.md](../../EXAMPLE-KALSHI-DASHBOARD-05-PHASE-3.md)
- [../../EXAMPLE-KALSHI-DASHBOARD-06-PHASE-4.md](../../EXAMPLE-KALSHI-DASHBOARD-06-PHASE-4.md)

## Reproduction Bar

- keep each phase dependency-closed
- do not start the next phase until the current one validates cleanly
- do not mix backend ingest, API/auth, and UI work into one prompt unless the feature is truly small
