x=int(input("Enter the value : "))
print("Factors are: ")
for i in range(1,x,1):
    if x%i==0:
        print(i, end=" ")
        i+=i
    if i==x:
        print("\n")
        print("Perfect number,mate")
    