import streamlit as st
import plotly.express as px
from core import load_data,reconcile

st.set_page_config(page_title="Finance Close Reconciliation",layout="wide")
st.title("Finance Close & Reconciliation Platform")
st.caption("Synthetic demonstration of deterministic matching, exceptions, duplicate controls, and human review.")
inv,bank=load_data()
res=reconcile(inv,bank)
counts=res.status.value_counts()
c=st.columns(4)
c[0].metric("Transactions",len(res))
c[1].metric("Auto Matched",int((res.status=="AUTO_MATCH").sum()))
c[2].metric("Exceptions",int((res.status!="AUTO_MATCH").sum()))
c[3].metric("Auto-Match Rate",f"{(res.status=='AUTO_MATCH').mean():.1%}")
status=counts.rename_axis("status").reset_index(name="count")
st.plotly_chart(px.bar(status,x="status",y="count",title="Reconciliation outcomes"),use_container_width=True)
st.subheader("Exception queue")
st.dataframe(res[res.status!="AUTO_MATCH"].sort_values(["status","amount"],ascending=[True,False]),use_container_width=True)
st.subheader("Matched transactions")
st.dataframe(res[res.status=="AUTO_MATCH"].head(100),use_container_width=True)
