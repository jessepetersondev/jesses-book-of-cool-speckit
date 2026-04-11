# Kalshi Quant Dashboard Phase 2 Prompt

Observed source: `/home/ai/.codex/history.jsonl`, session `019d7c0f-6eff-7920-85ac-aab67a3bc180`

```text
[$speckit-implement](/home/ai/clawd/projects/kalshi-quant-dashboard/.agents/skills/speckit-implement/SKILL.md) Implement Phase 2 only for 001-quant-ops-dashboard.

Before coding, read spec.md, plan.md, data-model.md, contracts/*, quickstart.md, and tasks.md. Identify the exact task IDs for this phase and any prerequisites, then implement only that set.

Phase 2 scope:
- Implement the canonical normalized event model in code and schema.
- Include ordering and replay metadata wherever available, including source sequence or ordinal, redelivery flags, replay/backfill markers, published/received/first-seen timestamps, source envelope identifiers, exchange, queue, routing key, delivery metadata, and adapter/source version.
- Implement the strategy registry and generic adapter framework so new strategies onboard via configuration and contract mapping.
- Implement real ingestion adapters for the current mixed-source reality using the local sibling repos:
  - ../kalshi-btc-quant
  - ../kalshi-eth-quant
  - ../kalshi-sol-quant
  - ../kalshi-xrp-quant
  - ../kalshi-integration-event-publisher
  - ../kalshi-integration-executor
- Implement direct strategy payload ingestion, centralized publisher ingestion, executor lifecycle/result ingestion, skip-only/no-trade diagnostic ingestion, heartbeat ingestion, and RabbitMQ management metric ingestion.
- Implement durable persistence for decisions, trades, skips, alerts inputs, queue metrics, heartbeats, positions, and normalized source events.
- Implement idempotency, deduplication, replay safety, and redelivery-safe convergence.
- Preserve raw source metadata needed for audit and troubleshooting.
- Implement basic reconciliation primitives for missing terminal events and stale live streams if they are in this phase’s task set.

Do not implement the full operator UI in this run.

Validation required:
- migration and schema updates pass
- ingestion integration tests pass against representative fixtures
- replay/redelivery tests prove ordered convergence
- skip-only/no-trade inputs are first-class and not inferred from missing orders
```
