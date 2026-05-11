x='Python is great and Java is also great'
y=[]
n=x.split()
for i in n:
    if i not in y:
        y.append(i)
print(y)

result=' '.join(y)

print(result)