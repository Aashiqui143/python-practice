a=int(input("Enter the row start = "))
b=int(input("Enter the row end = "))
c=int(input("Enter the difference = "))
d=int(input("Enter the column range = "))

for i in range(a,b,c):
    for j in range(d):
        print(i, end=" ")
        i=i+1
    print()