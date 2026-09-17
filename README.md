# Finance Close & Reconciliation Platform

A rules-driven finance automation platform for multi-source reconciliation, exception management, variance analysis, approval controls, and close-process reporting.

> **Working public demo:** Includes deterministic synthetic invoices and bank transactions, a working reconciliation engine, exception routing, an interactive Streamlit app, tests, and run instructions. See [`DEMO.md`](DEMO.md).

> **Portfolio note:** Public examples use synthetic data and generalized rules; no employer data, customer information, credentials, or proprietary source code are included.

## Try It

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Business Problem

Finance close processes often require analysts to compare multiple source systems, identify mismatches, classify exceptions, investigate variances, and document resolution. Manual spreadsheet workflows are slow, difficult to audit, and highly dependent on individual process knowledge.

## Demo Scenarios

The synthetic generator deliberately creates:

- exact matches
- near-amount variances
- partial payments
- missing references
- unknown payers
- duplicate transactions

The reconciliation engine then produces an auto-match population and a reviewable exception queue with scores and variance context.

## Reference Architecture

```text
CRM / ERP / Contract / Bank Data
                  |
                  v
             Normalization
                  |
                  v
            Rules Engine
                  |
         +--------+--------+
         |                 |
         v                 v
    Auto-Matched       Exceptions
                           |
                           v
                  Human investigation
                           |
                           v
                    Approval / audit
```

## Technology

`Python` `Streamlit` `Pandas` `Plotly` `Azure Functions` `Snowflake` `SQL` `Excel` `APIs` `Finance Controls`

## Repository Structure

```text
.
├── app.py
├── core.py
├── synthetic.py
├── requirements.txt
├── DEMO.md
├── docs/
│   ├── case-study.md
│   ├── architecture.md
│   ├── business-rules.md
│   ├── reconciliation-methodology.md
│   ├── data-dictionary.md
│   ├── security.md
│   └── runbook.md
└── tests/
    └── test_core.py
```

## Demo Status

- [x] Public-safe project definition
- [x] Synthetic reconciliation dataset
- [x] Deterministic matching engine
- [x] Exception classification
- [x] Duplicate / partial-payment controls
- [x] Interactive exception dashboard
- [x] Automated tests
- [ ] Hosted live-demo URL
- [ ] Recorded walkthrough

## Control Principle

AI may eventually summarize or classify exceptions, but it does not independently post or alter financial records. Deterministic rules, auditability, and human approvals remain authoritative.
