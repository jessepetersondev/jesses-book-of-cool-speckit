# Dashboard API Contract Summary

- overview, strategy, decision, trade, skip, alert list, and alert detail endpoints are required
- live update delivery uses SSE with capability-aware filtering
- export and raw payload access stay behind explicit authorization checks
- `/alerts/:alertId` remains a dedicated detail route across API and UI
