class plane:

    def __init__(self,name):
        self.name=name
        self._status=None


    def checking_status(self):
        print('connecting airrline company/airport api...')
        print(f'checking flight {self.name} status')
        return 1

    

    @property #属性方法，将方法变成一个属性（变量） 
    def flight_status(self):
        
        if self._status==0:
            print(f'{self.name} is flying')
        elif self._status==1:
            print(f'{self.name} is arrived')
        else:
            print('cannot confirm the flight status')

    @flight_status.setter #改变方法属性的方法，当改变flight_status时自动调用，当使用flight_status属性时自动调用属性方法
    def flight_status(self,status):
        self._status=status
        print('changing...flight status',self._status)



s=plane('J')
s.flight_status=1
s.flight_status
s.flight_status=0
s.flight_status

