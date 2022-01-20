# List of alternate prime numbers
a=int(input("Enter the value : "))
list1=[]
for i in range(2,a,1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        #print(i)
        list1.append(i)     
print(list1)
#r=list1[1:2]
#print(r)
for i in range(0,len(list1),2):
    print(list1[i])
    