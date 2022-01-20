amount=int(input("Enter the amount: "))
print("when you enter the amount, you get this many number of notes")
if amount%100==0:
    if amount>=500:
        a=amount//500
        bal=amount-(500*a)
        if bal>=200:
            b=bal//200
            againBal=bal-(200*b)
            if againBal>=100:
                c=againBal//100
                rest=againBal-(100*c)
                print("500 rupee notes are = ",a)
                print("200 rupee notes are = ",b)
                print("100 rupee notes are = ",c)
else:
    print("The amount entered is invalid.  Please Enter the amount in multiples of 100 only")
print("\n")
print("\n")
print("\n")
#Amount=int(input("Enter the Amount: "))
print("Generally, in",amount,"if you want to how it can be divided by 500 notes or 200 notes or 100 notes, then in ",amount,"you will have : ")
if amount%100==0:
    if amount>100:
        x=amount//100
        print("No. of 100 notes in ",amount," are = ",x," (Incase, If you want whole amount in only 100 notes) ")
    if amount>200:
        y=amount//200
        print("No. of 200 notes in ",amount," are = ",y," (Incase, If you want whole amount in only 200 notes) ")
    if amount>500:
        z=amount//500
        print("No. of 500 notes in ",amount," are = ",z," (Incase, If you want whole amount in only 500 notes) ")
else:
    print("Entered Amount is Invalid")

