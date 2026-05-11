redball=[]
blueball=[]
while len(redball)<6:
    while True:
        try:
            
            num=int(input(f'请选择第{(len(redball)+1)}个红球的号码'))
            result1 =f"{num:02d}"
            if num>=1 and num<33 and result1 not in redball:
                redball.append(result1)
                break
            else:
                print('输入不合法，请输入1到32其中的数字，并且不能重复')
                    
        except ValueError:
            print('请输入整数')

try:
    num=int(input('请选择蓝球的号码'))
    result1 =f"{num:02d}"
    if num>=1 and num<=16:
        blueball.append(result1)
        
    else:
        print('输入不合法，请输入1到16其中的数字')
     
    
except ValueError:
    print('请输入整数')

print(f'您选择的号码串是{redball+blueball}')











        
    
    
    
    
    
