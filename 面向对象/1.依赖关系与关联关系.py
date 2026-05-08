class Dog:

    d_type='哈士奇'#属性,类属性，类变量,公共属性
    attack_value=30
    life_value=150

    def __init__(self,name,age,master):#初始化方法，构造方法，构造函数，实例化时会自动执行，进行一些初始化的工作
        self.name=name
        self.age=age
        self.master=master#master应该为一个对象，这是一种关联关系，关联关系是指在A类长期持有B类（如成员变量，属性），这种结构性较依赖关系更强，视为A关联B
        self.sayhi()
    

    def sayhi(self): #方法,第一个参数必须是self,self代表实例本身
        print(f'你好，我是一条狗,我的品种是{self.d_type},名字是{self.name}，我今年{self.age}岁了,我的主人是{self.master.name}')

class Human:


    def __init__(self,name,age,from_):
        self.name=name
        self.age=age
        self.from_=from_
        self.sayhi()#在实例化的时候调用自己的方法
    
        if self.age>=18:
            self.attack_value=50
            self.life_value=200
        else:
            self.attack_value=20
            self.life_value=100

    def sayhi(self):
        print(f'你好，我来自{self.from_},名字是{self.name}，今年{self.age}岁了')

    def walk_dog(self,dog_obj):
        print(f'{self.name}带着他的狗{dog_obj.name}去散步')#依赖关系,依赖关系是最弱的一种类之间的联系，只有在要用到时临时使用，一般是以方法参数或局部变量的形式出现


p1=Human('李华',21,'山东')
p2=Human('小张',15,'北京')
d1=Dog('旺财',3,p1)
d2=Dog('大黄',5,p2)
p1.walk_dog(d2)

    
