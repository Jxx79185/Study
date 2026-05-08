import random

n=random.randint(1,100)

prompt='请输入你猜的值：'
while True:
    i=int(input(prompt))
    try:
        
        if i<n:
            prompt='猜错了，请再试一次，这次往更大的数字猜：'
        elif i>n:
            prompt='猜错了，请再试一次，这次往更小的数字猜：'
        elif i==n:
            print('恭喜你，猜对了')
            break

    except ValueError:

        print('请输入有效的数字')
        prompt = '请重新输入'


