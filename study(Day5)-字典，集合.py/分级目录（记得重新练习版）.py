menu = {
    '北京':{
        '海淀':{
            '五道⼝':{
                'soho':{},
                '⽹易':{},
                'google':{}
                },
            '中关村':{
                '爱奇艺':{},
                '汽⻋之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
        },
    },
        '昌平':{
            '沙河':{
                '路⻜学城':{},
                '北航':{},
            },
            '天通苑':{},
            '回⻰观':{},
},
        '朝阳':{},
        '东城':{},
},
    '上海':{
        '闵⾏':{
            "⼈⺠⼴场":{
                '炸鸡店':{}
}
},
        '闸北':{
            '⽕⻋站':{
                '携程':{}
}
},
        '浦东':{},
},
    '山东':{},
}

path=[menu]
x=True
while True:
    dangqian=path[-1]
    for list1 in path[-1]:
        if x:
            print(list1)
    choice=input('>=')
    if choice in dangqian:
        if  dangqian[choice]:
            path.append(dangqian[choice])
            x=True
        else:
            print('已经到最后一层')
            x=False
    elif choice=='b':
        if len(path)>1:
            path.pop()
            x=True
        else:
            print('已经返回到最高一层')
    elif choice=='e':
        break
    else:
        print('输入错误地址')
        