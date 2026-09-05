---
name: manual-trading-desk
description: Review stock candidates interactively with Codex, current research, and repository scoring rules. Use for manual paper-only analysis; never use it to place, modify, or close orders.
---

# Manual Trading Desk

Operate as an interactive research desk. This replaces paid model API calls with the current Codex session; it does not make the autonomous desk subscription-backed.

## Safety boundary

- Never import or invoke `stock_executor.py`, `crypto_executor.py`, or `src.desk`.
- Never submit, modify, cancel, or close an order. Never change `mode` to `live` or use the live acknowledgement flag.
- Treat every result as research for human review. A passing score means `REVIEW`, not permission to transact.
- Stop if candidate facts are stale, incomplete, contradictory, or not attributable to a source.

## Workflow

1. Read the candidate JSON supplied by the user. Use [references/stock-review.md](references/stock-review.md).
2. Verify time-sensitive market, company, news, and filing facts with current authoritative sources. Record source URLs and observation times.
3. Fill every analysis field conservatively on a 0–1 scale. Missing evidence receives the pessimistic value documented in the reference.
4. Save the completed packet outside tracked source files, normally under `manual_runs/`.
5. Run `python scripts/manual_review.py stock --input <packet.json>`. It uses deterministic scoring and hard vetoes without importing execution code.
6. Present the score, every component, veto reason, evidence freshness, and a clear `REVIEW` or `REJECT` label. Do not convert it into an order instruction.

If asked to place a trade, explain that this workflow is analysis-only and request a separate explicit decision outside this skill.
