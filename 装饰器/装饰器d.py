def outer(origin):#origin就是原函数，即被装饰的函数，这里是func
    def inner():
        print('before')
        res = origin() #在inner中的恰当位置执行原函数，并将值赋给新的变量  
        print('this is a outer' )
        return res #返回变量的值给inner()，所以func的函数值为inner的函数值，即res,即原函数的函数值
    return inner #将inner返回给装饰函数，此时outer(origin)的值即为inner,所以当fuc=outer(func),此时fuc=inner
                    #所以fuc()=inner(),即此时函数就已经完全等于inner了。

@outer
def func(): #9行和10行的语句等同于func=outer(func)
    print('this is a func')
    value=[1,2,3,4]
    return value
func()
    
# func=outer(func)
# func()

print(func())

def value():
    return 5

i=value()
print(i)