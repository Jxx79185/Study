import random


age = random.randint(1,100)
prompt='请输入你猜的年龄'

n=0
while n<3 :
    guess_number=int(input(prompt))
    if guess_number>age:
        prompt='不对，请再猜一次,这次往小了猜'
    
    elif guess_number<age:
        prompt='不对，请再猜一次,这次往大了猜'
    n+=1
    
    if guess_number==age:
        print('恭喜你猜对了')
        break
    
answer=input('是否还要继续猜，请输入‘yes’或者‘no’')

if answer in ['yes','y','Y']:
    while True:
        guess_number=int(input(prompt))
        if guess_number>age:    
            prompt='不对，请再猜一次,这次往小了猜'
        
        elif guess_number<age:
            prompt='不对，请再猜一次,这次往大了猜'
        n+=1
        
        if guess_number==age:
            print('恭喜你猜对了')
            break
else:
    print(f'good bye,顺便告诉你答案是{age}')
        




        
