students = [("小明", 88), ("小红", 95), ("小刚", 78)]
number=[-9,3,-8,79,8]
print(type(students))
# 按成绩排序（升序）

number.sort()
print(number)
number.sort(key=lambda s:s**2)#根据列表number中的数字的三次方的大小进行排序
print(number)
students.sort(key=lambda s:s[1])#根据列表中的嵌套列表的索引为1的，以编码的字符顺序进行排序
print(students)
students.sort(key=lambda s:len(s[0]))#根据列表中的嵌套列表的索引为0的字符串长度进行排序
print(students)




squared=list(map(lambda s:s**2,number))#根据函数内容对数据进行批量处理
print(squared)


evens=list(filter(lambda s:s>0,number))#根据函数内容对数据进行过滤
print(evens)

