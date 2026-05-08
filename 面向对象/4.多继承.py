class ShenXian:#父类
    def fly(self):
        print('神仙可以飞')
    
    def fight(self):
        print('神仙在打架')

class Monkey:#父类
    def eat_peach(self):
        print('猴子都喜欢吃桃子')

    def fight(self):#当父类方法出现冲突会依据优先级进行继承,使用C3算法
        print('猴子在打架')

class SunWuKong(ShenXian,Monkey):#子类，可以继承很多父类，并且会继承父类的父类
    def gold_stick(self):
        print('孙悟空在使用金箍棒')

m1=SunWuKong()
m1.fly()
m1.eat_peach()
m1.fight()
print(SunWuKong.mro())#查看一个子类继承父类的C9算法优先级