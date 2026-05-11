any_list = ['yes','none','why','yes','go','go','none','go']

last_pos = {}
for idx, item in enumerate(any_list):
    last_pos[item] = idx  # 更新元素最后出现的位置

# 按元素最后出现的顺序排序
result = list(last_pos.keys())         # Python 3.7+ 字典保留插入顺序
# 或显式排序（兼容旧版本）
result = sorted(last_pos, key=lambda x: last_pos[x])

print(result)  # 输出 ['yes', 'none', 'why', 'go']