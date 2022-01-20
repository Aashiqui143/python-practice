pr_marks=int(input("Enter the project marks: "))
i_marks=int(input("Enter the internal marks: "))
e_marks=int(input("Enter the external marks: "))
if pr_marks>=50:
    print()
else:
    print("you have failed in Project Marks, Because your marks '",pr_marks,"' are less than 50")
if i_marks>=50:
    print()
else:
    print("you have failed in Internal Marks, Because your marks '",i_marks,"' are less than 50")
if e_marks>=50:
    print()
else:
    print("you have failed in External Marks, Because your marks '",e_marks,"' are less than 50")
if pr_marks>=50 and i_marks>=50 and e_marks>=50:
    print()
else:
    print("As you have failed in your subjects,you are not gonna get grade, mate. Better luck next time. ")
if pr_marks>=50:
    if i_marks>=50:
        if e_marks>=50:
            total_score=0.7*pr_marks+0.2*e_marks+0.1*i_marks
            print("Total score = ",total_score)
            if total_score>=90:
                print("A Grade")
            elif total_score>=75 and total_score<90:
                print("B Grade")
            elif total_score>=50 and total_score<75:
                print("C Grade")
