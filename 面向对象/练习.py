class SuperMarket:

    def __init__(self,name,money):
        self.name=name
        self.__money=money
        self.item={}

    def add_item(self,obj):
        self.item[obj]=obj

    def sell(self,obj):
        self.__money+=obj.value

    def all_money(self):
        print(self.__money)

    def buy(self,obj):
        self.__money-=obj.value

class Convenience(SuperMarket):
    def __init__(self, name, money):
        super().__init__(name, money)

    

class Item:
    def __init__(self,name,value):
        self.name=name
        self.value=value

def deal(buyer,seller,item):
    buyer.buy(seller.item[item])
    seller.sell(seller.item[item])


s1=SuperMarket('永辉',20000)
s2=SuperMarket('万家乐',30000)
patato=Item('patato',15)
s2.add_item(patato)

deal(s1,s2,patato)
s1.all_money()
s2.all_money()

class Car:
    def horn(self):
        print('1')
        return '滴滴'

class Trunk:
    def horn(self):
        print('2')
        return '嗡嗡'
    
def horn(name):
    print(name.horn)


horn(Car())
horn(Trunk())




        

