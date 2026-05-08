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
# __import__('test') #当用户使用字符串，用字符串格式用这个方法导入包。
import importlib#使用动态模块导入的标准库
# importlib.import_module('test')#python官方推荐导入方法

def load_moudle(name):
    importlib.import_module(name)

load_moudle('test')


