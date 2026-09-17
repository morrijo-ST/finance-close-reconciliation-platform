# Reconciliation Methodology — Finance Close & Reconciliation Platform

## Match Priority
Rules are evaluated in an explicit order so the same inputs produce the same outcome.

### M-001 — Exact Match
Reference key and amount match exactly.

### M-002 — Tolerance Match
Reference key matches and amount variance falls within the configured tolerance.

### M-003 — Secondary / Fuzzy Match
Primary reference is missing or inconsistent, but approved secondary evidence such as payer, date proximity, and amount supports a candidate match.

### M-004 — Partial Match
The reference aligns but the financial amount represents only part of the source balance.

### M-005 — Duplicate Candidate
The same reference and amount appear more than once within the configured detection window.

### M-006 — Materiality Review
Even an otherwise valid match requires approval when it exceeds the configured materiality threshold.

### M-007 — Unresolved
No approved rule produces a sufficient match; route to the exception queue.

## Match Output
Each reconciliation result stores:
- source record identifiers
- rule applied
- variance amount
- match score where applicable
- status
- reviewer / approval details
- timestamps

## Design Principle
The reconciliation engine should favor explainability and auditability over opaque probabilistic matching.