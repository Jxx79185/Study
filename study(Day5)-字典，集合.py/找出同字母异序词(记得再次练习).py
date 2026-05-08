arr=['cat','dog','tac','god','act']
dic=dict()
for i in arr:
    x=list(i)
    x.sort()
    x=tuple(x)
    if x not in dic:
        dic[x]=[i]
    else:
        dic[x].append(i)

print(dic)

    