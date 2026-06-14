import re
def read():
    with open("statement.txt","r",encoding="utf-8") as f:
        lines=[line.strip() for line in f]

    trxn=[]
    i=0
    while i<len(lines):
        if re.fullmatch(r"\d{2}-\d{2}-\d{4}",lines[i]):
            date=lines[i]
            # print(date)
            j=i+1
            while j<len(lines) and lines[j]=="":
                j+=1
            payee=lines[j]
            # print(payee)
            i=j+1

            amt=None 
            rembal=None
            k=j+1
            while k<len(lines):
                m = re.match(r"([\d,]+\.\d{2})\s+([\d,]+\.\d{2})", lines[k])
                # \d matches the amout d{2} matches the decimal number  
                # followed by space again to match balance \d+ and d{2} for the amt.00 
                if m:
                    amt=  float(m.group(1).replace(",",""))
                    # print(amt)
                    
                    rembal=float(m.group(2).replace(",",""))
                    # print(rembal)
                    break
                k=k+1
            
            if date and payee and amt:
                trxn.append({
                    "date": date,
                    "payee":payee,
                    "amount": amt,
                    "remaining bal":rembal}
                )
            i=k+1
        else:
            i+=1
    return trxn 

read()
