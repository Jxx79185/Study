list1=[]
with open('study(附加)/学籍注册.txt','r',encoding='utf-8') as f: 
    for line in f:
        line=line.strip().split(',')
        list1.append(line)
    
cl=['python','linux','网络安全','前端','数据分析']
prompt='您要进行学籍注册服务吗？是请输入1，退出请输入2：'
while True:
    choice=input(prompt)
    if '1' in choice:
        name=input('姓名：')
        age=input('年龄：')
        phone_num=input('手机号：')
        id = input('身份证号')
        class1=input('所选课程:')

        list2=[name,age,phone_num,id,class1]

        if all(x[2]!=phone_num for x in list1):
            if all(x[3]!=id for x in list1):
                if class1 in cl:
                    list1.append(list2)
                else:
                    print('可选课程只能从python，linux，网络安全，前端，数据分析里面进行选择')
                    continue
            else:
                print('不能和已有的身份证号相同')
                continue
        else:
            print('不能和已有的电话号码相同')
            continue

        

        with open('study(附加)/学籍注册.txt','w',encoding='utf-8') as f:
            for i in list1:
                line=','.join(map(str,i))
                f.write(f'{line}\n')
                prompt='您要继续进行学籍注册服务吗？是请输入1，退出请输入2：'

    elif '2' in choice:
        break



    
    
    # if 
    # dic['姓名']=name
