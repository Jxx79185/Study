menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '路飞学城': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

current_layers = [menu]  # 当前层的字典栈
current_path = []        # 用户访问路径栈

while True:
    current_layer = current_layers[-1]
    
    # 显示路径信息
    path_display = '>='.join(current_path) if current_path else "根目录"
    print(f"\n当前路径: {path_display}")
    
    # 显示当前层选项
    if current_layer:
        print("可选目录:")
        for key in current_layer:
            print(f"  {key}")
    else:
        print("⚠️ 当前目录无下级选项")
    
    # 获取用户输入
    choice = input("\n请输入目录名继续 (b-返回/e-退出): ").strip()
    
    # 处理退出
    if choice.lower() == 'e':
        print("退出导航系统")
        break
        
    # 处理返回
    if choice.lower() == 'b':
        if len(current_layers) > 1:
            current_layers.pop()
            current_path.pop()
            print(f"↩ 已返回到: {' -> '.join(current_path) if current_path else '根目录'}")
        else:
            print("⛔ 已是最顶层")
        continue
        
    # 处理有效目录选择
    if choice in current_layer:
        next_layer = current_layer[choice]
        
        if next_layer:
            current_layers.append(next_layer)
            current_path.append(choice)
            print(f"✅ 进入: {choice}")
        else:
            print("⚠️ 这是最后一级目录，请直接返回(b)或退出(e)")
    else:
        print(f"⛔ 无效输入，请从下列选项中选择: {', '.join(current_layer.keys()) or '无'}")

