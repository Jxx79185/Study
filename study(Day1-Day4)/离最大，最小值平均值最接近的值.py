ant_list=[1,8,9,156,9,158,12,48,51,489,123,4869,1256,46]
a=[96,89,78,54,12,85,8,4,56]


def method1(list):
    list.sort()
    print(list)
    average=(list[0] + list[-1])/2
    print(average)
    
    cha=abs(average-list[0])
    for i1 in list:   
        if abs(average-i1) < cha:
            cha=abs(average-i1)
            i2=i1
    print(i2)

    



method1(ant_list)
method1(a)



