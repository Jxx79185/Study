menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '⽹易':{},
                'google':{}
                },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
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
    '⼭东':{},
}

# 使用栈维护菜单层级
path = [menu]

while True:
    current_layer = path[-1]
    
    # 打印当前层级选项
    for key in current_layer:
        print(key)
    
    choice = input("请输入选项（b返回/q退出）: ").strip()
    
    if choice == 'b':
        if len(path) > 1:
            path.pop()  # 返回上一级
        else:
            print("已是最顶层")
    elif choice == 'q':
        break  # 退出程序
    elif choice in current_layer:
        next_layer = current_layer[choice]
        if next_layer:  # 非空子菜单
            path.append(next_layer)
        else:
            print("已到达最底层")
    else:
        print("无效输入，请重新选择")