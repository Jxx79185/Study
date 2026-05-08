def check_int(func):
    def wrapper(*args):
        for i,v in enumerate(args):
            if not isinstance(v,int):
                raise TypeError(f'参数{i+1}不是整数，您输入的是{type(v)}')
        return func(*args)
    return wrapper

@check_int
def sum1(a,b):
    return a+b

print(sum1(11,12))