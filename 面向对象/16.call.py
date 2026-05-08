#call方法,对象后面加括号执行

class School():
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr

    def __call__(self, *args, **kwds):
        print('call已执行')


s=School('荣昌中学','荣昌')

print(s)

s()
        
