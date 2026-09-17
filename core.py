import pandas as pd
from synthetic import generate_reconciliation_data

def load_data(invoice_path=None, bank_path=None):
    if invoice_path is None or bank_path is None:
        return generate_reconciliation_data()
    inv=pd.read_csv(invoice_path,parse_dates=["invoice_date"])
    bank=pd.read_csv(bank_path,parse_dates=["transaction_date"])
    return inv,bank

def reconcile(inv,bank):
    invx=inv.set_index("invoice_id")
    seen=set()
    rows=[]
    for _,t in bank.iterrows():
        ref=t["reference"] if pd.notna(t["reference"]) else ""
        key=(ref,round(float(t["amount"]),2))
        variance=None
        if key in seen and ref:
            status="DUPLICATE"; score=0
        elif ref in invx.index:
            i=invx.loc[ref]
            variance=float(t["amount"])-float(i["invoice_amount"])
            pct=abs(variance)/float(i["invoice_amount"]) if i["invoice_amount"] else 1
            if abs(variance)<0.01:
                status="AUTO_MATCH"; score=100
            elif pct<=.02:
                status="REVIEW_VARIANCE"; score=90
            elif float(t["amount"])<float(i["invoice_amount"]):
                status="PARTIAL_PAYMENT"; score=75
            else:
                status="REVIEW"; score=60
        else:
            status="UNMATCHED"; score=0
        seen.add(key)
        rows.append({**t.to_dict(),"status":status,"match_score":score,"variance":variance})
    return pd.DataFrame(rows)
