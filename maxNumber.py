
fmax=0
smax=0
for i in range(5):
    num=int(input("Enter the number: "))
    if fmax<num:
        smax=fmax
        fmax=num
        
print("Maximum number: ",fmax)
print("Second maximum number: ",smax)