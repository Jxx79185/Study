#第一种方法
# test=[4,6,6,4,2,2,4,8,5,8]

# dic=dict()

# for i in test:
#     if i not in dic:
#         dic[i]=[i]
      

#     else:
#         dic[i].append(i)


# print(dic)


#第二种方法
# test=[4,6,6,4,2,2,4,8,5,8]

# dic=dict()

# for i in test: 
#      if i not in dic:
#         dic[i]=[i] *test.count(i)

# print(dic)

#output{4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}