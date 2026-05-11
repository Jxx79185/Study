import random
data1=[5,6,5,4,6,5]
data2=[5,4,5,6,4,5]

m=random.choice(data1)
n=random.choice(data2)

if m+n==10:
    print([m,n])

else:
    print('此次随机值的和不为10')
