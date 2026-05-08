import json

# 原始数据
data = {"水果": ["苹果", "香蕉"], "数量": 3}

# 序列化
json_str = json.dumps(data)
print("这是字符串：", type(json_str))  # <class 'str'>
print(json_str)

# 反序列化
new_data = json.loads(json_str)
print("变回字典：", type(new_data))   # <class 'dict'>
print(new_data)