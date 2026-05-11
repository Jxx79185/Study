def info(name,age,phone,*args,**kwargs):
    inf=f'''
    Name:{name},
    Age:{age},
    phone:{phone}
    '''
    print(inf)
    print(args)
    print(kwargs)

dic={'name':'jiang','phone':'17623215104','age':'24'}
# info('jiang',24,'17623215104','game',hobbie='anime')
info('syou',sex='file',phone='1789416485',age=18)
info(**dic)