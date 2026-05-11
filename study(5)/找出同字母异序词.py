arr=['cat','dog','tac','god','act']
dic=dict()
for i in arr:
    to_key=list(i)
    to_key.sort
    to_key=tuple(to_key)
    if to_key not in dic:
        dic[to_key]=[i] #生成一个字典的key与value
    else:
        dic[to_key].append(i)

print(list(dic.values()))
