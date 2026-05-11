import random

staff_list=[f'{i:03d}'for i in range(1,301)]
prompt='开始抽奖\n'
for n in range(30):
    input(prompt)
    number=random.choice(staff_list)
    print(f'恭喜{number}号的员工中了三等奖')
    staff_list.remove(number)
    prompt=""
prompt=f"恭喜这30位员工获得三等奖，还有{len(staff_list)}位员工没有中奖，让我们开始第二轮抽奖\n"

n=0
input()
for n in range(6):
    input(prompt)
    number=random.choice(staff_list)
    print(f'恭喜{number}号的员工中了二等奖')
    staff_list.remove(number)
    prompt=""
prompt=f'恭喜这6位员工获得二等奖，还有{len(staff_list)}位员工没有中奖，让我们开始第三轮抽奖\n'
n=0
input()
for n in range(3):
    input(prompt)
    number=random.choice(staff_list)
    print(f'恭喜{number}号的员工中了一等奖')
    staff_list.remove(number)
    prompt=''
print()
print(f'恭喜这3位员工获得一等奖')

