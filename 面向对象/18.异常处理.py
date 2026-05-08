name=input('请输入校名')
age=input('请输入校龄')

try:
    def __init__(self,addr):
        self.addr=addr
    School=type('School',(),{
        'name':name,
        'age':age,
        '__init__':__init__
        })
    
    s=School('荣昌')
    print(s.name)

except NameError as e:
    print('有没有定义的变量')

except ValueError as e:
    print('数据类型错误')

except Exception as e:#保底处理
    print('未知错误')

else:
    print('没有异常进行运作')

finally:
    print('无论有没有异常都走这里')


class MyException(BaseException):#定义自定义异常
    def __init__(self,msg):
        self.message=msg

    def __str__(self):
        return self.message
    
try:
    raise MyException('出现自定义异常')#主动触发自定义异常

except MyException as e:#进行异常捕捉
    print(e)
    


