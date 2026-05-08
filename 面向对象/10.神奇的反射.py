import sys
#可以通过字符串的形式来操作对象的属性
class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age

    def walking(self):
        print('He is walking.')


p = Person('Alex',15)
if hasattr(p,'name'):#映射，当检测p实例是否拥有name属性。
    print('iru')

#四个方法
# getattr()#get获取
a=getattr(p,'age')
print(a)

# hasattr()#has判断
user_command=input('>>:').strip()
if hasattr(p,user_command):
    func=getattr(p,user_command)
    func() 

# setattr()#set赋值

setattr(p,'sex','Female')#设置了个静态属性
print(p.sex)

def talking(self):
    print('He is talking')
setattr(Person,'speak',talking)#直接给类一个新的方法

p.speak()
# delattr()#del删除



#如何访问一个文件下指定的字符串对应的属性
print(__name__)#__main__代表模块本身
if __name__=='__main__':#只会在被别的模块导入时发挥作用, __name__在当前模块主动执行的情况下（不是被导入执行），等于__main__，被导入时等于模块本身的名字
    print('hhhhh')  
    # __name__在当前模块主动执行的情况下（不是被导入执行），等于__main__
mod = sys.modules[__name__]#代表模块本身



