
x=int(input("Enter the value : "))
y=0
for i in range(1,x+1,1):
    if x%i==0:
        y+=1
print("No. of factors are: ",y)
    
if y>2:
    print(i," is not a prime number")
elif y==2:
    print(i," is a prime number" )
else:
    print(i," is neither prime nor composite")