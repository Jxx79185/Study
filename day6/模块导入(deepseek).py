import sys
import os
import pprint

# 获取绝对路径
current_file = os.path.abspath(__file__)
print(current_file)
project_root = os.path.dirname(os.path.dirname(current_file))
mod_path = os.path.join(project_root, 'mod')

# 创建目录（如果不存在）
os.makedirs(mod_path, exist_ok=True)

# 添加到 Python 路径
if mod_path not in sys.path:
    sys.path.insert(0, mod_path)

# 验证路径和模块是否存在
print("mod_path:", mod_path)
print("moduel.py 是否存在:", os.path.exists(os.path.join(mod_path, 'moduel.py')))

# 尝试导入
try:
    import moduel
    moduel.sayhi()
except Exception as e:
    print("导入失败，错误信息:", e)