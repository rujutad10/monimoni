import format
from datetime import datetime
import pandas as pd
from collections import defaultdict

trxn=format.read()
def date():
    
    datesort=sorted(
        trxn,
        key=lambda x:datetime.strptime(x['date'],"%d-%m-%Y"),
        reverse=True

    )
    df = pd.DataFrame(datesort)

    print(df.to_string(index=True))

def amt():
    byamt=sorted(trxn,key=lambda x:x['amount'],reverse=True)
    df = pd.DataFrame(byamt)

    print(df.to_string(index=True))

def payee():
    clus=defaultdict(list)
    for t in trxn:
        clus[t['payee']].append(t)
    tot=0
    for payee, tr in clus.items():
        print(payee)
        tot=0
        for t in tr:
            print(f"{t['date']} {t['amount']}") 
            tot+=t['amount']
     
        print(f"\nfor {payee}, total spent is {tot}\n")
