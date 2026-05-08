class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __len__(self):
        print('trigger...')
        return 0

    def __getitem__(self,item):
        self.item=item
        print('get item',self.__dict__[self.item])
    
p=Person('小明',18)
len(p)
p['name']#会将‘name’视为‘item’传进去


class School():
    def __init__(self,name,addr,type):
        self.name=name
        self.addr=addr
        self.typr=type

    def __repr__(self):#执行repr方法输出
        return f'{self.name},{self.addr}'
    
    def __str__(self):#执行str方法输出，如果没有str方法则由repr方法代替输出，如果两个方法都没又输出实例
        return f'hahahhah{self.name},{self.addr}'

a=School('荣昌中学','荣昌区','高中')

print(repr(a))
print(str(a))
print(a)#相当于使用str(a)输出字符串类型的实例表示

#直接使用str函数或者print函数调用实例时--->obj.__str__()
#直接使用repr或者交互器解释器中调用实例时--->obj.__repr__()
#注意，返回值必须为字符串，否则会抛出异常