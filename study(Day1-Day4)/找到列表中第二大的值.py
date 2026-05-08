ant_list=[1,8,9,156,9,158,12,48,51,489,123,4869,1256,46]
max_int=ant_list[0]
smaller_int=ant_list[0]
for i in ant_list:  
    if max_int<i :
        max_int=i

ant_list.remove(max_int)

for i in ant_list:  
    if smaller_int<i :
        smaller_int=i
    

    
print(smaller_int)
print(max_int)
        
ant_list.sort()
print(ant_list)