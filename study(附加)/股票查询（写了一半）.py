data=[]
file_path='study(附加)/gupiao.txt'
with open(file_path,'r',encoding='utf-8') as f:
    for line in f:
        line=line.strip().split(',')
        data.append(line)

def search_str(target):
    result=[]
    for sublist in data:
        if any(target in str(item) for item in sublist):
            result.append(sublist)  
    return result

def search_area(project,fuhao,value):
    if project in data[0]:
        position=data[0].index(project)
        if '>' in fuhao:
            print(data[0])
            for data1 in data[1:-1]:
                v=float(data1[position].strip().rstrip('%'))
                if v>float(value):
                    print(data1)
        if '<' in fuhao:
            print(data[0])
            for data1 in data[1:-1]:
                v=float(data1[position].strip().rstrip('%'))
                if v<float(value):
                    print(data1)



        


print('''
      请选择您的查询方式
        1.根据字符进行模糊查询
        2.数值条件筛选
        3.退出''')
chioce=input('')
if chioce=='1':
    tar=input('请输入您要查找的字符')
    if '>' or '<' or'=' not in tar:
        result=search_str(tar)
        for i in result:
            print(i) 

elif chioce=='2':
    project=input('请输入您要查询哪一项?')
    fuhao=input("请输入您要查询的值为'>','=','<'?")
    value=input('请输入值')
    search_area(project,fuhao,value)

    
    
        


   