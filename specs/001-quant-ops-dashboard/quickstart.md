# Quickstart

1. compile or refresh the phase packs with `python3 scripts/reconcile-phase-packs.py --root . --feature 001-quant-ops-dashboard`
2. verify the packs are current with `python3 scripts/verify-phase-pack-freshness.py --root . --feature 001-quant-ops-dashboard`
3. use the compiled pack for the current phase only
4. if the phase changes canonical truth, reconcile again before the next phase
