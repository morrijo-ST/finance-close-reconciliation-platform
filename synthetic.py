import numpy as np
import pandas as pd

def generate_reconciliation_data(seed=42):
    rng=np.random.default_rng(seed)
    invoices=[]
    for i in range(1,221):
        amt=round(float(rng.uniform(500,50000)),2)
        invoices.append([f"INV-{i:05d}",f"CUST-{rng.integers(1,91):04d}",amt,pd.Timestamp("2026-01-01")+pd.Timedelta(days=int(rng.integers(0,180)))])
    inv=pd.DataFrame(invoices,columns=["invoice_id","customer_id","invoice_amount","invoice_date"])
    bank=[]; tid=1
    for _,r in inv.iloc[:150].iterrows():
        bank.append([f"TXN-{tid:05d}",r.invoice_id,r.customer_id,r.invoice_amount,r.invoice_date+pd.Timedelta(days=int(rng.integers(1,14))),"exact"]); tid+=1
    for _,r in inv.iloc[150:170].iterrows():
        bank.append([f"TXN-{tid:05d}",r.invoice_id,r.customer_id,round(r.invoice_amount*rng.uniform(.985,1.015),2),r.invoice_date+pd.Timedelta(days=5),"near_amount"]); tid+=1
    for _,r in inv.iloc[170:190].iterrows():
        bank.append([f"TXN-{tid:05d}",r.invoice_id,r.customer_id,round(r.invoice_amount*rng.uniform(.4,.8),2),r.invoice_date+pd.Timedelta(days=7),"partial"]); tid+=1
    for _,r in inv.iloc[190:200].iterrows():
        bank.append([f"TXN-{tid:05d}","",r.customer_id,r.invoice_amount,r.invoice_date+pd.Timedelta(days=6),"missing_ref"]); tid+=1
    for i in range(10):
        bank.append([f"TXN-{tid:05d}",f"INV-X{i}",f"UNKNOWN-{i}",round(float(rng.uniform(500,10000)),2),pd.Timestamp("2026-05-01")+pd.Timedelta(days=i),"unknown"]); tid+=1
    for b in bank[:5]:
        tid+=1; bank.append([f"TXN-{tid:05d}",b[1],b[2],b[3],b[4],"duplicate"])
    bankdf=pd.DataFrame(bank,columns=["transaction_id","reference","customer_id","amount","transaction_date","scenario"])
    return inv,bankdf
