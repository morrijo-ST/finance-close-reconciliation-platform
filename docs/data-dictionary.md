# Data Dictionary — Finance Close & Reconciliation Platform

| Table | Field | Type | Description |
|---|---|---|---|
| source_a | record_id | string | Primary record key from source A |
| source_a | reference_id | string | Reconciliation reference |
| source_a | amount | decimal | Source A financial amount |
| source_a | record_date | date | Source A transaction date |
| source_b | record_id | string | Primary record key from source B |
| source_b | reference_id | string | Reconciliation reference |
| source_b | amount | decimal | Source B financial amount |
| source_b | record_date | date | Source B transaction date |
| reconciliation | reconciliation_id | string | Reconciliation result key |
| reconciliation | source_a_id | string | Matched source A key |
| reconciliation | source_b_id | string | Matched source B key |
| reconciliation | match_rule | string | Rule identifier used |
| reconciliation | match_score | decimal | Match confidence / score |
| reconciliation | variance_amount | decimal | Amount difference |
| reconciliation | status | string | matched / exception / approved / rejected |
| reconciliation | reviewer | string | Synthetic reviewer identifier |
| reconciliation | reviewed_at | datetime | Review timestamp |
| exception | exception_type | string | Duplicate / partial / missing reference / tolerance / unresolved |
| exception | explanation | string | Investigation note |

All public records are synthetic and designed to demonstrate reconciliation scenarios.