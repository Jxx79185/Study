list1=[['a','b'],'c','d','e']
list2=['a','b']
list3=['c','d']
r=True
for i in list3:
    if i not in list1:
        print('list2不是list1的子列表')
        r=False
        break
    

if  r:
    print('list2是list1的子列表')

        

    
    

