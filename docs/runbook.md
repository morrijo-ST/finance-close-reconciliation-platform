# Operations Runbook — Finance Close & Reconciliation Platform

## Run Sequence
1. Confirm all source files / tables are complete for the close period.
2. Validate row counts and required keys.
3. Normalize reference IDs, dates, and numeric fields.
4. Execute matching rules in priority order.
5. Review duplicate and partial-match exceptions.
6. Route material exceptions to authorized reviewers.
7. Reconcile resolved totals to source controls.
8. Export close-status and exception-aging reports.

## Common Failures
### Source imbalance
Stop the run and confirm the expected source population before matching.

### Duplicate explosion
Review source duplication and matching-key quality before changing rules.

### Excess unmatched records
Inspect reference normalization, date windows, amount tolerances, and missing source records.

### Reviewer bottleneck
Prioritize by materiality and aging; maintain explicit ownership.

## Recovery
Reruns must preserve original source evidence and produce reproducible results for the same rule version and inputs.

## Manual Override
Authorized finance reviewers may resolve an exception manually, but the original values, rationale, reviewer, and timestamp remain in the audit history.