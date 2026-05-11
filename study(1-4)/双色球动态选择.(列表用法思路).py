red_balls=[]
blue_balls=[]

li=[[6,32,'红球',red_balls],[1,16,'篮球',blue_balls]]
for item in li:
    while len(item[3])<item[0]:
        while True:
            try:
                num = int(input(f'请选择第{len(item[3])+1}个{item[2]}的号码'))
                result1=f"{num:02d}"
                if num >=1 and num <= item[1] and result1 not in item[3]:
                    item[3].append(result1)
                    break
                else:
                    print(f'输入不合法，请输入1到{item[1]}其中的数字，并且不能重复')
            except ValueError:
                print('请输入整数')

print(f'您选择的号码是{red_balls+blue_balls}')