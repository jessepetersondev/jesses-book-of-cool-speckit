# Quant Ops Dashboard Plan

## Architecture

- normalize inbound events into a canonical trading-operations model
- persist converged state so replay and redelivery are safe
- expose REST and SSE surfaces behind capability-aware enforcement
- keep the React operator UI as the final phase so it builds on validated backend contracts

## Phase Boundaries

- `initial-build`: establish the canonical artifacts
- `pre-implement-revision`: repair contradictions before coding
- `strict-phased-mode`: lock the phase order and dependency boundaries
- `phase-2`: ingestion, persistence, replay safety
- `phase-3`: auth, capability resolution, API, SSE
- `phase-4`: operator UI and route-level validation
