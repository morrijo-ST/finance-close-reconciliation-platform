from core import load_data,reconcile

def test_reconcile():
    inv,b=load_data()
    r=reconcile(inv,b)
    assert (r.status=='AUTO_MATCH').sum()>=145
    assert (r.status=='DUPLICATE').sum()>=5
