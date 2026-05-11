def year_money(m,n,x):#m为本金，n为要到达的金额,x为利息倍数
    year=0
    while True:
        year+=1
        m=m*x
        print(f'第{year}年后可取的现金为{m}')
        if m>n:
            print(f'第{year}年后存款可到达理想金额')
            break

year_money(10000,20000,1.0325)   
    