import format
import sort
import time 
print("\n")
print("hello! welcome to monimoni")
print("to get started copy your bank statement and save it as 'statement.txt'")

time.sleep(3)
while True:
    start = input("Press 0 if you have added the file: ")

    if start == "0":
        break

    print("Please try again")

trxn=format.read()
print("\n")
print("great! we have processed your data")
time.sleep(1)
print("choose what you would to do next:")
time.sleep(1)
print(
    "0. exit\n"
    "1. sort by date\n" 
    "2. sort by payee\n"
    "3. sort by amount\n"
    "4. find maximum trxn amount"
)
time.sleep(2)
x=0
while x!=1:
    try:
        n = int(input("enter number according to your choice: "))
    except ValueError:
        print("invalid input,please try again")
        
    if n==1:
        sort.date()
    elif n==2:
        sort.payee()
    elif n==3:
        sort.amt()
    elif n==4:
        max_trxn = max(trxn, key=lambda x: x['amount'])
        print(f"max transaction was {max_trxn['payee']} with amount: {max_trxn['amount']}")
    elif n==0:
        print("\nthank you for using monimoni<3")
        x=1
    else:
        print("invalid, please try again")