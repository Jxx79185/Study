class Chikhen:
    def __init__(self,type,price,number):
        self.type=type
        self.price=price
        self.number=number

f_ch=Chikhen('f',5,1)
m_ch=Chikhen('m',3,1)
l_ch=Chikhen('l',1,3)

for f in range(21):
    for m in range(34):
        for l in range(301):
            if f+m+l==100 and (f*5)+(m*3)+(l/3)==100 and l%3==0:
                print(f'可以买公鸡{f}只,母鸡{m}只，小鸡{l}只')
                


