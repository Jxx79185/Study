dic12= {
"Alex":[23,'0123458',"CEO",66000],
"⿊姑娘":[24,'748952','行政',4000],
"佩奇":[26,'9542145',"讲师",40000]
}



# def chaxun(dic):
#     while True:
#         name=input('请输入你要查询的人的姓名')
#         info=dic.get(name)
#         if name not in dic:
#             print('此姓名不存在')
#             continue
#         else:
#             print(f'{name}，其年龄为{info[0]},电话为{info[1]}，职业为{info[2]}，薪资为{info[3]}')
#             return False

# chaxun(dic12)


for i in dic12:
    print(i,dic12[i])


