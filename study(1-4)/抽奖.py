import random
number_list=[f'{i:03d}'for i in range(1,301)]

for n in range(30):
    people=random.choice(number_list)
    print(f'恭喜{people}号的同事中了三等奖,避孕套20盒。')
    number_list.remove(people)
    input()

n=0
print(f'还有{len(number_list)}位同事没有中奖')
input('接下来抽2等奖')

for n in range(6):
    people=random.choice(number_list)
    print(f'恭喜{people}号的同事中了二等奖,Iphone Plus 12手机一台。')
    number_list.remove(people)
    input()

n=0
print(f'还有{len(number_list)}位同事没有中奖')
input('接下来抽1等奖')

for n in range(3):
    people=random.choice(number_list)
    print(f'恭喜{people}号的同事中了一等奖,泰国5日游加手术费报销')
    number_list.remove(people)
print(f'剩下的{len(number_list)}位同事只有等下一回了')


