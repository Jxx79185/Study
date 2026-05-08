def input_list():
    while True:
        try:
            s=input('请输入一个整数列表，元素用逗号隔开:').strip()

            if not s:
                print('输入不能为空,请重新输入')
                continue

            elements=[]
            s=s.replace('，',',')
            for part in s.split(','):
                part=part.strip()
                try:
                    num=int(part) 
                    elements.append(num)
                except Exception as e:
                    print('数据必须为整数，请重新输入')
                    break
            print(elements)
            return elements
        except Exception as e:
            print('未知错误')


                
list1=input_list() 



def paixu(n):
    if not isinstance(n,list):
        raise TypeError('参数必须为列表类型')
    i=0
    for i in range(1,len(n)):
        tmp=n[i]
        j=i-1
        while tmp<n[j] and j>=0:
            n[j+1]=n[j]
            j-=1
        n[j+1]=tmp
    
    print(n)

paixu(list1)

                
             

    

