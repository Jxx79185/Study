li_s=[]
balance=int(input('请输入您的余额为多少元？'))
print(f'以下为我们的商品列表'.center(50,'-'))


li=[[1,'可乐',5],[2,'花生',15],[3,'瓜子',10],[4,'牛奶',30],[5,'薯片',20],[6,'香皂',35],[7,'大米',40],[8,'饼干',50],[9,'方便面',25]]

for item in li:
    print(f'{item[0]}号商品-----{item[1]}-----价格为{item[2]}')

while True:
    try:
        num=input('请输入你要购买商品的序号')
        
        

        if num == '结算' :
            break
        num=int(num)
        if 1<=num<=9 :  
            
            li_a=li[num-1]
            x=balance-li_a[2]

        else:
            print('请输入正确的序号1-9')
            continue 

        if x<0:
            print('您的余额不足,请换一种商品')
            continue
        
        if 1<=num<=9 :  
            
            li_s.append(li_a)
            balance-=li_a[2]
            print(f'您购买了序号{li_a[0]}的商品{li_a[1]},花费{li_a[2]}元，您目前的余额为{balance}元')
        

        
        
        
        
                


    except ValueError:
        print('请输入正确的序号，为整数1-9。')

print(f'您购买的商品列表为'.center(50,'-'))
for i in li_s:
    print(f'{i[0]}号商品-----{i[1]}-----价格为{i[2]}元')


print(f'您最后剩下的余额为{balance}')




    

# for item in li :
#     while True:
#         try:
#             num=int(input('请输入你要购买商品的序号'))
#             if num == item[0]
            











#         except ValueError:
#             print('请输入正确的序号，为整数1-9。')