name = ['Alex','li','金角大王']
s=name[7:9]

print(name.index('li'))

name.append('32')#增
name[1]='lii'#改
name.index('Alex')#查
name.remove('lii')#删
del name[1]#删
name.insert(1,'112')#插入

print(name)

s='jida da'
s.title()
print(s.removeprefix('j'))#去掉片头的字符

n='The Great Wall in China'
list=n.split()
print(list)

print('-'.join(list))

