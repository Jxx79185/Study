class Dog:
    name='d'
    def __init__(self,name):
        self.name=name

    @classmethod
    def eat(cls):
        print(cls)
        print(f'dog {cls.name} is eating')



d1=Dog('dd')
d1.eat()
#类方法，不能访问实例变量，只能访问类变量，因为在@classmethod装饰器的装饰下self这个参数接收的不是实例本身，而是整个类

class Student:
    __stu_num=0
    def __init__(self,name):
        self.name = name 
        Student.__stu_num+=1
        print(f'生成了一个学生,{self.name}{self.__stu_num}')

    @property
    def get_stu_num(self):
        print(self.__stu_num)

    

    

s1=Student('a')
s2=Student('b')
s3=Student('c')

s3.get_stu_num
#将公共信息存储到类变量里面，可以用类方法操作