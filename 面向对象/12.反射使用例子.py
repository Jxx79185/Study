class User:
    def login(self):
        print('登录')

    def register(self):
        print('注册')

    def save(self):
        print('存储')

u=User()
while True:
    user_cmd = input('>>:').strip()
    if hasattr(u,user_cmd):#通过反射可以控制u这个实例里面的方法执行，如果不这样想要在确认实例里面是否有方法再进行执行的话，就得一个一个写
        func=getattr(u,user_cmd)#获取方法
        func()#执行


