class Student:
    role='学生'

    def __init__(self,name):
        self.name=name

    @staticmethod  #静态方法，不能访问类变量也不能访问实例变量，静态方法割断了它跟类和实例的任何关系
    def fly(self):
        print(f'{self.name}is flying')

s=Student('d')
s.fly(s)#不会自己传入self，需要手动传入。