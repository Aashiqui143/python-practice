units=int(input("Enter the no. of units = "))
if units<=50:
    bill=50*0.75
elif units>50 and units<=150:
    bill=50*0.75+(units-50)*2.10
elif units>150 and units<=250:
    bill=50*0.75+100*2.10+(units-150)*2.50
else:
    bill=50*0.75+100*2.10+100*2.50+(units-250)*2.80
print("\n")
print("\n")
print(bill)
gst=0.1*bill
Bill=gst+bill
print("After adding gst, Total bill will be ",Bill)