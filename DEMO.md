# Run the Public Demo

This repository includes a deterministic synthetic-data demo. No external credentials or proprietary datasets are required.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Run tests with:

```bash
pytest -q
```

The demo creates invoices and bank transactions with exact matches, near-amount variances, partial payments, missing references, unknown payers, and duplicates, then routes the results through a deterministic reconciliation engine and exception queue.
