class Student():
    def __init__(self,name,cls):
        self.name=name
        self.cls=cls
        print('__init__已执行')

    def __new__(cls,*args,**kwargs):#构造方法
        #会先创建一个空对象 super().__new__(cls)
        #在把这个对象传给init做初始化
        print(f'__new__已执行,cls为{cls,args,kwargs}')
        return super().__new__(cls)
        #__new__方法掌握__init__的执行,进行一些初始化之前的操作，如果不重写__new__，原本会调用__init__,自己重写后如果不调用则不会执行__init__

p=Student('小明',3)
print(p.cls)

#单例模式的实现（比如有些窗口在生成之后如果不关闭不会生成第二个，即不会生成第二个实例）

#以打印机为例，用word打印，pdf打印，excel同时打印，三个打印任务会给同一个打印程序处理

# class Printer():
    
#     tasks = []
#     def __init__(self,name):
#         self.name = name
        
        

#     def add_task(self,job):
#         self.tasks.append(job)
#         print(f'添加任务{job}到打印机')

# p1= Printer('word app')
# p2= Printer('pdf app')
# p3= Printer('excel app')

# p1.add_task('word job')
# p2.add_task('pdf job')
# p3.add_task('excal job')
# 这样会导致生成3个实例，从而生成3个打印任务，如果是打印同样的东西会比较浪费资源



class Printer():
    
    tasks = []
    _instance=None
    def __init__(self,name):
        self.name = name
        
    def add_task(self,job):
        self.tasks.append(job)
        print(f'添加任务{job}到打印机')

    def __new__(cls,*arg,**kwargs):
        if cls._instance is None:
            #当没有这个类没有任何一个实例时，进行正常的实例化
            cls._instance = super().__new__(cls)
            print(cls._instance)
        return cls._instance#将初次实例化的对象存到instance中，第二次实例化不再生成新的实例直接返回存储的第一个实例
        #即单例模式
p1= Printer('word app')
p2= Printer('pdf app')
p3= Printer('excel app')

print(p1,p2,p3)
print(p1.name,p2.name,p3.name)
#最后会发现这三个的name属性都是同一个，也就是最后一个赋值的'excel app'，因为第一次创建实例后，
# 就不会再创建新的实例，但会执行__init__初始化将实例的初始属性进行一次修改，就成了name为最后一次生成的name
#这就是单例模式的实现（比如有些窗口在生成之后如果不关闭不会生成第二个，即不会生成第二个实例）




