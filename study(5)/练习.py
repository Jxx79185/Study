import random
staff_list={'syou':[24,'python','60000'],'girlfriend':[25,'AI','12000'],'xiaoyun':[22,'student',5000]}

names={'xiaoyun':[25,'data',10000],'Sam':[36,'CEO',60000]}

staff_list.update(names)

print(staff_list)
x=[]
for i in staff_list:
    x.append(i)

list={11:22,33:44,55:66}

x=list.items()
print(x)

for i in list:
    print(i)


n=['da','ws','dwe','da']
print(n.index('da'))

j=dict.fromkeys(n,random.randint(1,100))
print(j)

print(ord('√'))




