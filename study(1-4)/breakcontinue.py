def process_floors():
    for floor in range(1, 7):
        print(f'当前在第{floor}层'.center(10, '-'))
        if floor == 3:
            continue
        
        for room in range(10):
            if floor == 4 and room == 4:
                print('??????')
                return  # 直接退出函数，终止所有循环
            print(f'当前在{floor}0{room}室')

process_floors()