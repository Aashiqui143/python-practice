sal=float(input("Enter the salary = "))
if sal>0:
    if sal<10000:
        da=0.7*sal
        hra=0.65*sal
        gross_salary=sal+da+hra
        print("Gross salary is ",gross_salary)
    elif sal>=10000 and sal<=20000:
        da=0.75*sal
        hra=0.73*sal
        gross_salary=da+hra+sal
        print("Gross salary is ",gross_salary)
    else:
        da=0.8*sal
        hra=0.76*sal
        gross_salary=da+sal+hra
        print("gross salary is ",gross_salary)
else:
    print("your salary is invalid")