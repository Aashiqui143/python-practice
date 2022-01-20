a=9
b=91
for i in range(5):
    for j in range(5):
        if i%2==0:
            a=a+1
            print(a,end=" ")
        else:
            b=b-1
            print(b,end=" ")
            
    print()   