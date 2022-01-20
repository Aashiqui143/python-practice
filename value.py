x=int(input("Enter the value : "))
list1=[]
for i in range(1,x):
    for value in range(1,i):
        if i%value==0:
            list1.append(i)
print(list1)