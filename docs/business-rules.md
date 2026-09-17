# Business Rules — Finance Close & Reconciliation Platform

**BR-001 — Exact match**  
Records with the same governed reference key and amount are eligible for automatic reconciliation.

**BR-002 — Tolerance match**  
A configurable variance threshold may classify near-matches for review but does not silently overwrite source values.

**BR-003 — Duplicate control**  
Potential duplicates are blocked from auto-resolution and routed to review.

**BR-004 — Partial match**  
Partial payments or partial contract values remain explicitly classified and cannot be treated as full matches.

**BR-005 — Missing reference**  
Transactions with missing primary keys require secondary matching evidence or manual review.

**BR-006 — High-value approval**  
Transactions above the configured materiality threshold require human approval even when an exact match is found.

**BR-007 — AI limitation**  
AI may summarize supporting evidence but cannot independently change the accounting outcome.

**BR-008 — Source preservation**  
Original source values remain immutable within the reconciliation process.

**BR-009 — Rule traceability**  
Each resolved record stores the rule identifier and resolution timestamp.

**BR-010 — Exception aging**  
Open exceptions retain status and aging until formally resolved or closed with documented rationale.