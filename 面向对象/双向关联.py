class RealationShip:#使两个对象双向关联
    def __init__(self):
        self.couple=[]

    def make_couple(self,obj1,obj2):
        self.couple=[obj1,obj2]

    def get_my_partner(self,obj):
        print(f'寻找{obj.name}的对象')
        for n in self.couple:
            if n!=obj:
                print(f'对象为{n.name}')
                return n
        else:
            print('你没点逼数吗？你有对象吗？')
        
class Person:
    def __init__(self,name,sex,realation,girlfriend=None):
        self.name=name
        self.sex=sex
        self.girlfriend=girlfriend
        self.realation=realation

realation_obj=RealationShip()
p1=Person('li','m',realation_obj)
p2=Person('wang','f',realation_obj)

print(realation_obj.couple[0].name)
print(realation_obj.couple[1].name)

