import random

n = 10  # 列表长度
min_val = 1
max_val = 100

random_list = [random.randint(1, 100) for _ in range(n)]
print(random_list)
# 示例输出: [34, 72, 15, 88, 5, 97, 61, 3, 42, 90]