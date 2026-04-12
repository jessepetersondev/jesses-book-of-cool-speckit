# Kalshi Example Corpus

This file documents the concrete Kalshi repos that were used as the source material for the framework.

These are examples, not the framework itself.

If you are trying to decide what to read first, start with [KALSHI-EXAMPLES.md](KALSHI-EXAMPLES.md).

## Shared Setup Observed Across The Example Corpus

- bootstrap command in shell history:
  `specify init . --ai codex --ai-skills --force`
- observed `speckit` version:
  `0.5.1.dev0`
- observed integration:
  `codex`
- observed extensions:
  none

## Example Repos

| Repo | Example Role |
|---|---|
| `/home/ai/kalshi-edge-saas` | greenfield narrow SaaS build |
| `/home/ai/kalshi-edging-quant` | brownfield approved-delta migration |
| `/home/ai/clawd/projects/kalshi-quant-dashboard` | phased multi-implement build |
| `/home/ai/clawd/projects/kalshi-weather-quant` | multi-repo migration |
| `/home/ai/clawd/projects/kalshi-integration-event-publisher` | related integration boundary repo |

## Why Keep This File

The framework in this repo is generic, but it was not invented abstractly. It was derived from repeated real runs across these repos, which is why the command structure and prompt shapes are grounded rather than hypothetical.
