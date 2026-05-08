class Dog:
    d_type = '哈士奇'
    attack_value = 30

    def __init__(self, name):
        self.name = name
        self.__life_value = 150  # 私有属性，不能被外部访问以及修改

    def attack(self, obj):#攻击方法，由于不能直接修改其他对象的私有属性，采用一种方法，让对象自己调用自己的方法来修改对象的私有属性
        obj.be_attacked(self.attack_value)
        print(f'{self.d_type}{self.name}攻击了{obj.name},造成了{self.attack_value}点伤害,{obj.name}还剩下{obj.get_life_value()}点血')

    def be_attacked(self, damage):#被攻击的方法，是和其他对象交互的接口，其他对象可以通过让本对象自己调用这个方法来形成交互
        self.__life_value -= damage

    def get_life_value(self):
        return self.__life_value

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weapon = Weapon(self)
        if self.age >= 18:
            self.attack_value = 50
            self.__life_value = 200
        else:
            self.attack_value = 20
            self.__life_value = 100

    def be_attacked(self, damage):
        self.__life_value -= damage

    def get_life_value(self):
        return self.__life_value

class Weapon:
    def __init__(self, user):
        self.user = user

    def dog_stick(self, obj):
        self.name = '打狗棒'
        self.attack_value = 70
        obj.be_attacked(self.attack_value)
        self.print_log(obj)
        return 'haha'

    def knife(self, obj):
        self.name = '屠龙刀'
        self.attack_value = 100
        obj.be_attacked(self.attack_value)
        self.print_log(obj)

    def gun(self, obj):
        self.name = 'AK47'
        self.attack_value = 150
        obj.be_attacked(self.attack_value)
        self.print_log(obj)

    def print_log(self, obj):
        print(f'{self.user.name}使用{self.name}进行了攻击,造成了{self.attack_value}点伤害,{obj.name}还剩下{obj.get_life_value()}点血量')

# 测试代码
d1 = Dog('大黄')
p1 = Human('丽', 18)
d1.attack(p1)
p1.weapon.dog_stick(d1)
p1.weapon.knife(d1)