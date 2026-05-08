ant_list=[1,8,9,156,9,158,12,48,51,489,123,4869,1256,46]
x=len(ant_list)
for j in range(x):
    for i in range(x-1-j):
        if ant_list[i]>ant_list[i+1]:
            ant_list[i],ant_list[i+1]=ant_list[i+1],ant_list[i]

print(ant_list)
