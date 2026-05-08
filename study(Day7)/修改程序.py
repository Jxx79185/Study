data={'username':['username','password','age','position','department','phone'],
      'alex':['alex','abc123','30','Engineer','IT','13651830433'],
      'rain':['rain','df2@432','25','Teacher','Teching','18912334223'],
      '黑姑娘':['黑姑娘','df2@432','26','行政','人事','13811177306']}
while True:
    n=input('Username:')
    p=input('Password:')
    #登录，输入用户名密码，记住用户名

    if n in data:
        if p==data[n][1]:
            print(f'welcome,{n}'.center(50,'-'))
            break
        else:
            print('密码不正确，请重新输入')
            continue
    else:
        print('用户名不存在，请重新输入')
        continue
    #如果用户名密码对应正确，进入欢迎界面，
    

def pr_info(info):
    print(f'Name:{data[info][0]}')
    print(f'Age:{data[info][2]}')
    print(f'Position:{data[info][3]}')
    print(f'Department:{data[info][4]}')
    print(f'Phone:{data[info][5]}')
#打印个人信息的方法函数

def change_info(info):
    i=0
    while i<=5:
        print(f"{i}.{data['username'][i]}:{data[info][i]}")
        i+=1
    j=int(input('请选择你要修改的个人信息:'))
    print(f'您所选择的旧信息为：{data[info][j]}')
    new_j=input('请输入您修改的信息：')
    data[info][j]=new_j
    print(f"修改成功，您的新{data['username'][j]}为{new_j}")
    print('您的各项信息为：')
    pr_info(info)


while True:
    choice=input('''
请选择您要进行的服务:
1.打印个人信息
2.修改个人信息\n''')
    if choice=='1':
        pr_info(n)
    elif choice=='2':
        change_info(n)
    elif choice=='q':
        print('很高兴为您服务，bye')
        break
    else:
        print('不清楚您的指令,请重新输入')



    


    







