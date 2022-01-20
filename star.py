for i in range(6):
    for j in range(7):
        if i==0:
            if j%3!=0:
                print("*",end=" ")
        if i==1:
            if j%3==0:
                print("*",end=" ")
        if i==2:
            if j==5 or j%6==0:
                print("*",end=" ")
        
            
            
        