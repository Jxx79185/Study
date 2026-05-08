# any_list=['yes','none','why','yes','yes','go','go','none','go']
# new_list=[]

# for i in any_list:
#     if   i not in new_list:
#         new_list.append(i)

# print(new_list)
#生成一个新列表把旧列表第一次出现的值添加进去




# any_list=['yes','none','why','yes','yes','go','go','none','go']
# new_list=[]

# for i in any_list:
#     if any_list.count(i) >1 and new_list.count(i)<1:
#         new_list.append(i)

# print(new_list)
# for j in new_list:
#     count_num=any_list.count(j)
#     if j in any_list:
#         for x in range(count_num-1):
#             any_list.remove(j)

# print(any_list)

#生成一个新的列表记录重复的字符，把这些字符从原来的列表中去掉到只剩一次

any_list=['yes','none','why','yes','yes','go','go','none','go']

set=set(any_list)

print(set)

list = list(set)

print(list)






