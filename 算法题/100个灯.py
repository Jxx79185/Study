lights=[False]*100

for i in range (1,101):
    for j in range (i-1,100):
        if (j+1)%i==0:
            lights[j]=not lights[j]


close_light=sum(1 for state in lights if not state)

print(close_light)



