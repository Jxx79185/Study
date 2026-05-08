ant_list=[1,8,9,156,9,158,12,48,51,489,123,4869,1256,46]


j=0
for x in range(len(ant_list)-j):
    i = 1 
    while True:
        if i>=len(ant_list):
            j+=1
            break
        elif ant_list[i-1]>ant_list[i]:
            ant_list[i-1],ant_list[i]=ant_list[i],ant_list[i-1]
        i+=1

print(ant_list)
    
    


