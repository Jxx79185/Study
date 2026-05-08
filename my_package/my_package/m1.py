import sys
import pprint
import os
pprint.pprint(os.getcwd())
path=os.path.dirname(os.path.dirname(os.getcwd()))
pprint.pprint(path)
data_path=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0,data_path)
pprint.pprint(sys.path)
from my_package2.my_package2 import m2
print(os.listdir())