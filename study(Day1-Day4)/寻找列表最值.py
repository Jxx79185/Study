list_=[9,5,8,4,6,48,64,89,512,545,4813,21,564,186,15,16]
m=list_[0]
n=list_[0]
for i in list_:
    
    if int(i)>m:
        m=i
    if int(i)<n:
        n=i

    
    
print(m,n)
