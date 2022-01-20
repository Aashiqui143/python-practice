'''amount=int(input("Enter the amount: "))
if amount%10!=0:
    print("Invalid amount")
else:
    
    if amount>10:
        a=amount//10
        print("no,of 10 rupee notes in amount is ",a)
    if amount>20:
        b=amount//20
        print("no. of 20 rupee notes in amount is ",b)
    if amount>50:
        x=amount//50
        print("No. of 50 notes in ",amount," are = ",x," (Incase, If you want whole amount in only 50 notes) ")
    if amount>100:
        y=amount//100
        print("No. of 100 notes in ",amount," are = ",y," (Incase, If you want whole amount in only 100 notes) ")
    if amount>200:
        z=amount//200
        print("No. of 200 notes in ",amount," are = ",z," (Incase, If you want whole amount in only 200 notes) ")'''

amount=int(input("Enter the amount: "))
if amount%10==0:
    print("valid amount")
    if amount>=200:
        b=amount//200
        amount=amount-(200*b)
        print("200 rupee notes are =  ",b)
    if amount>=100:
        c=amount//100
        amount=amount-(100*c)
        print("100 rupee notes are =  ",c)
    if amount>=50:
        d=amount//50
        amount=amount-(50*d)
        print("50 rupee notes  are = ",d)
    if amount>=20:
        e=amount//20
        amount=amount-(20*e)
        print("20 rupee notes are = ",e)
    if amount>=10:
        f=amount//10
        rest=amount-(f*10)
        print("10 rupee notes are = ",f)
    
   
   
  