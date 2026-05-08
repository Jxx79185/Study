from collections import defaultdict

# 输入函数封装(带校验)
def input_students(class_name):
    while True:
        try:
            n = int(input(f'请输入{class_name}有多少学生：'))
            if n <= 0:
                print("请输入大于0的整数！")
                continue
            break
        except ValueError:
            print("输入错误，请输入数字！")
    
    name_dict = defaultdict(int)
    for i in range(n):
        while True:
            name = input(f'请输入第{i+1}位同学姓名：').strip()
            if name:
                name_dict[name] += 1
                break
            print("姓名不能为空，请重新输入！")
    return name_dict

# 统计重复姓名
def get_duplicates(name_dict):
    return {name: count for name, count in name_dict.items() if count > 1}

# 主程序
print("=== 1班数据输入 ===")
class1 = input_students("1班")
print("\n=== 2班数据输入 ===")
class2 = input_students("2班")

# 处理分析结果
dup1 = get_duplicates(class1)
dup2 = get_duplicates(class2)
common_names = set(class1.keys()) & set(class2.keys())

# 交叉重复分析
cross_duplicates = {}
for name in dup1:
    if name in class2:
        cross_duplicates[name] = {
            'class1_count': class1[name],
            'class2_count': class2[name]
        }

# 输出结果
print("\n=== 分析结果 ===")
print(f"1班重复姓名数量：{len(dup1)}个，具体重复情况：")
for name, count in dup1.items():
    print(f"  - {name} 出现 {count} 次")

print(f"\n2班重复姓名数量：{len(dup2)}个，具体重复情况：")
for name, count in dup2.items():
    print(f"  - {name} 出现 {count} 次")

print(f"\n两班共同存在的姓名数量：{len(common_names)}个")
print("其中同时存在重复情况的姓名：")
for name, counts in cross_duplicates.items():
    print(f"  - {name}: 1班出现 {counts['class1_count']} 次，2班出现 {counts['class2_count']} 次")

print("\n=== 最终统计 ===")
print(f"1班共有 {len(dup1)} 个重复姓名")
print(f"2班共有 {len(dup2)} 个重复姓名")
print(f"两班共有 {len(common_names)} 个相同姓名")
print(f"其中 {len(cross_duplicates)} 个重复姓名在两班都有出现")