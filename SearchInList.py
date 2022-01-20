list1=[23,45,67,89,23,56,23]
count=0
x=int(input("Enter the variable: "))
for i in list1:
    if x==i:
        count+=1
if count!=0:
    print("yes, it is in the list")
    print("count = ",count)
else: 
    print("No, it is not in the list")
