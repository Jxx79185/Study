for i in range(2,101):
    is_primenumber=True
    for j in range(2,i):
        if  i%j==0:
            is_primenumber=False

    if is_primenumber==True:
        print(f'{i}是素数')
        
        
            