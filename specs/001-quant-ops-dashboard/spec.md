# Quant Ops Dashboard Spec

## Outcome

Build an operator-facing dashboard for quant trading operations with reliable live and historical views, explicit RBAC, and drill-down routes for decisions, trades, skips, alerts, and admin controls.

## Scope

- preserve a backend-first implementation sequence
- support mixed-source ingestion before any UI assumptions about unified upstream state
- expose live and historical parity for the operator flows that matter
- make detail pages deep-linkable and auditable

## Non-Goals

- do not broaden into full PnL analytics beyond the approved reporting surfaces
- do not skip validation or phase boundaries to force a one-pass build
