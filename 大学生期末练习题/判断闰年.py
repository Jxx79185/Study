while True:
    i=int(input('请输入你要判断的年数'))
    if i%4==0 and i%100!=0 or i%400==0:
        print(f'{i}是闰年')
    else:
        print(f'{i}不是闰年')

    j=input('是否继续')
    if j in '是':
        continue
    else:
        break