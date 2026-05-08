num1=[1,3,7,10,11,13]
num2=[3,7,8,9,19,20]
num=num2+num1
num.sort()
print(num)
n=len(num)
i=n//2
print(i)
if n%2!=0:
    num_mid=num[i]
    print(num_mid)

if n%2==0:
    num_mid=(num[i-1]+num[i])/2
    