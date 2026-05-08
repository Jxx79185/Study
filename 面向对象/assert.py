#assert语法用于判断代码是否符合执行预期
try:
    assert type(1) is str #如果不符合预期会报异常

except AssertionError:
    print('输出结果不符合预期')



#应用场景举例，别人调用你的接口，你的接口要求他调用的时候必须传递指定的关键参数，等他传递过来时检验他传过来的参数是否符合你的预期/


def my_interface(name,age,score):
    try:
        assert type(name) is str
        assert type(age) is int
        assert type(score) is float
    except AssertionError:
        print('输入的参数有误，请检查参数')
    else:
        print('生成成功')



my_interface('dd',18,89.456)