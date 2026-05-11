for i in range(2,101):
    n=int(i**0.5+1)
    
    for j in range(2,n):

        if i%j == 0:
            break

    else:
        print(f'{i}是素数')#当循环正常结束（没有被break，exit...）则执行。

