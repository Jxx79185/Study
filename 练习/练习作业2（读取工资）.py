
try:
    Money=int(input('你能输入你的月工资吗？让我来判断下你的心态'))

    if Money<1000:
        print('煞笔老板，老子今天想上班就上，不想上就不上你管得着吗？有本事把我开了')
    elif Money<2000:
        print('老子是你爹')
    elif Money<5000:
        print('去你的老板')
    elif Money<10000:
        print('经常背后区区老板')
    elif Money<20000:
        print('老板说错了，但我不反驳他')
    elif Money<30000:
        print('老板说啥就是啥，只要给钱')  
    elif Money<50000:
        print('老板肯定是对的，错的肯定是自己')
    elif Money<100000:
        print('996不过只是我略微出手罢了')
    else :
        print('把公司当成家')

except ValueError:
    print('请输入数字')