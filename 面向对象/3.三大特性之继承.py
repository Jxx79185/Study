class Animal:#父类
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex


    def eat(self):
        print(f'{self.name}正在吃东西')

class Human(Animal):#子类
    def __init__(self,name,age,sex,hobbie):
        # Animal.__init__(self,name,age,sex) #将父类的方法参数传入子类的构造方法
        super().__init__(name,age,sex)#效果同上(相当于调用父类的__init__方法)，并且在多继承中不会出现重复调用或者遗漏
        self.hobbie=hobbie

    def eat(self):
        super().eat()
        print(f'{self.name}正在使用筷子吃东西')

    def talk(self):
        print(f'{self.name}在讲话')

class Dog(Animal):#子类
    def __init__(self,name,age,sex):
        # Animal.__init__(self,name,age,sex) #将父类的方法参数传入子类的构造方法
        super().__init__(name,age,sex)#效果同上   

    def eat(self):
        super().eat()
        print(f'{self.name}正在用狗盆吃东西')

    def chase(self):
        print(f'{self.name}在进行捕猎')

p1=Human('LI',18,'m','anime')
d1=Dog('siro',3,'f')
p1.eat()
d1.chase()

        