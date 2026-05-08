for i in range(2,101):
    if all(i%j!=0 for j in range(2,i-1)):
        print(i)

       
     
            



