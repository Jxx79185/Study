def sorting(li):
    
    for i in range(len(li)):
        if i<len(li):
            k=i
        for j in range(i+1,len(li)):           
            if j<len(li) and li[k]>li[j]:
                    k=j
        if i!=k:       
            li[i],li[k]=li[k],li[i]
    print(f"排序后的顺序为{li}")
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


li=input_list()

sorting(li)