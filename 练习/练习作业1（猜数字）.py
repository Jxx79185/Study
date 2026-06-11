import random

n=random.randint(1,100)

prompt='请输入你猜的值：'
print('猜数字：请输入1-100之中的值')
while True:
    try:
        i=int(input(prompt))
        if i<0 or i >100:
            print('请输入1-100以内的数字')
            continue
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


