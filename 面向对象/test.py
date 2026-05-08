import sys
import os
import pprint


print(__file__)
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))

base_path=os.path.dirname(os.path.dirname(__file__))
mod_path=os.path.join(base_path,'mod')
os.makedirs(mod_path,exist_ok=True)

if mod_path not in sys.path:
    sys.path.insert(0,mod_path)
    #模块寻找路径
pprint.pprint(sys.path)
print('导入成功')

