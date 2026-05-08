#多态（Polymorphism）是面向对象编程的重要特性，指不同对象对同一方法调用能产生不同的行为。
class Animal:
    def __init__(self,name):    
        self.name=name
    def speak(self):
        raise NotImplementedError("子类必须实现 speak() 方法")

class Dog(Animal):
    def __init__(self,name,age):    
        super().__init__(name)
        self.age=age
    def speak(self):
        return "汪汪！"

class Cat(Animal):
    def speak(self):
        return "喵喵！"

def animal_sound(animal):
    print(animal.speak())

# 多态调用
a=Dog('旺财',18)
b=Cat('小黑')
animal_sound(a)  # 输出：汪汪！
animal_sound(b)  # 输出：喵喵！


