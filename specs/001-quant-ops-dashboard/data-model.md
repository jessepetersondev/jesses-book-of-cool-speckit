# Quant Ops Dashboard Data Model

- `normalized_events`: canonical event rows shared by ingest, API, and replay logic
- `strategy_health_views`: read-side aggregates for overview and strategy health
- `operator_alerts`: incident and alert records that support list and detail routes
- `auth_sessions` and `role_bindings`: identity and capability resolution inputs
