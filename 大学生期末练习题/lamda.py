def calculate_day_of_year(year, month, day):
    count = day
    month_map = {
        11: lambda: 30,
        10: lambda: 31,
        9:  lambda: 30,
        8:  lambda: 31,
        7:  lambda: 31,
        6:  lambda: 30,
        5:  lambda: 31,
        4:  lambda: 30,
        3:  lambda: 31,
        2:  lambda: 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28,
        1:  lambda: 31,
        0:  lambda: 0
    }
    
    # 模拟穿透行为
    for m in range(month - 1, -1, -1):
        if m in month_map:
            count += month_map[m]()
        else:
            print("error!")
            return None
    
    print(f"{year}年{month}月{day}日是该年的第{count}天！")
    return count


