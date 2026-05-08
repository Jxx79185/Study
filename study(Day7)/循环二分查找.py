你=[1,3,4,6,7,8,9,11,15,17,19,21,22,25,29,33,38,69,107,864,985,1986]
def findd(i,a):

    start=0
    end=len(a)-1
    while True:
            
        x=int((start+end)/2)
        x
        if len(a[start:end])==1:
            print('列表中没有找到这个值')
            break
        if a[x]>i:
            print(f'{i}小于{a[x]}，该在{a[start]}到{a[x]}里面去进行寻找')
            end=x
            
        elif a[x]<i:
            print(f'{i}大于{a[x]}，该在{a[x]}到{a[end]}里面去进行寻找')
            start=x

        else:
            print(f'找到了.在列表的第{x+1}个')
            break

findd(8,你)