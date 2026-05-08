def answer(number):
    s=0
    for i in range(1,number+1):
        if i%2==0:
            s=s-i
        if i%2!=0:
            s=s+i

    print(s)

answer(100)
