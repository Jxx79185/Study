#动态创建一个类

age=input('请输入校龄')


class School():

    def __init__(self,name,addr):
        self.name=name 
        self.addr=addr
    
    _age=age

    
s=School('荣昌中学','荣昌')


print(s._age)
print(type(s))
print(type(School))#类由type产生


type('Dog',)
