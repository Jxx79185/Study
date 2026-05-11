import copy
l='djiwd  daw'
n=list(l)
print(n)

print(n[::-1])#列表切片(反转)

print('d' in n)

a=['a','b','c','d',['e','f',['x','y']],'g']
print(id(a))
print(id(a[4]))
print(id(a[4][2]))
print(id(a[4][2][1]))
print()


b=copy.deepcopy(a)
print(id(b))
print(id(b[4]))
print(id(b[4][2]))
print(id(a[4][2][1]))