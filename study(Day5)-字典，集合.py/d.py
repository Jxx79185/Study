i=0
k=0
list1=[1,1,2,3,2,3,11,12,13,4,5,6,7,8,8,7,6,5,4,3,19,20,1,8,20,20,21]
while(i <len(list1)):
    member=list1[i]
    if list1.count(member)!=1:
        for j in range(list1.count(member)-1):
            list1.remove(member)
            i=k
    else:
        i=i+1
        k=i
print(list1)

