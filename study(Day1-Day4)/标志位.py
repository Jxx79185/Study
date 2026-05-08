exit_flag = False

for floor in range(1,7):
    for room in range(1,15):
        if room <10:
            print(f'当前是{floor}0{room}室')
        elif room >=10:
            print(f'当前是{floor}{room}室')
        
        if floor ==4 and room ==4:
            print('后面的房间都不见了')
            exit_flag = True
        break 
    if exit_flag:
        break
            
