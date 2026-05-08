#由一堆组件构成一个完整的实体，组件本身独立，但又不能自己运行，必须和宿主组合在一起运行

class Dog:

    d_type='哈士奇'#属性,类属性，类变量,公共属性
    attack_value=30
    life_value=150

    def __init__(self,name):#初始化方法，构造方法，构造函数，实例化时会自动执行，进行一些初始化的工作
        self.name=name
        

    def attack(self,obj):
        obj.life_value-=self.attack_value
        print(f'{self.d_type}{self.name}攻击了{obj.name},造成了{self.attack_value}点伤害,{obj.name}还剩下{obj.life_value}点血')

class Human:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.weapon=Weapon(self)#将当前人类实例传给武器

    
    
        if self.age>=18:
            self.attack_value=50
            self.life_value=200
        else:
            self.attack_value=20
            self.life_value=100

   
    
class Weapon:
    def __init__(self,user):#新增构造函数，接受使用者信息
        self.user=user      #武器使用者对象

    def dog_stick(self,obj):
        self.name='打狗棒'
        self.attack_value=70
        obj.life_value-=self.attack_value
        self.print_log(obj)

    def knife(self,obj):
        self.name='屠龙刀'
        self.attack_value=100
        obj.life_value-=self.attack_value
        self.print_log(obj)

    def gun(self,obj):
        self.name='AK47'
        self.attack_value=150
        obj.life_value-=self.attack_value
        self.print_log(obj)

    def print_log(self,obj):
        print(f'{self.user.name}使用{self.name}进行了攻击,造成了{self.attack_value}点伤害,{obj.name}还剩下{obj.life_value}点血量')

d1=Dog('大黄')
p1=Human('丽',18)
d1.attack(p1)
p1.weapon.dog_stick(d1)
p1.weapon.knife(d1)



        
        