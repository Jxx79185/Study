#狗大战
#1.多条狗，每个狗有名字，品种，攻击力
#2.可以有多个人。
#3.狗可以咬人，人可以打狗。

attack_value={
    'hasiqi':30,
    'zangao':100
}
#各种品种狗的攻击力

life_value={
    'hasiqi':200,
    'zangao':100,
}
#不同品种狗的生命

def dog(name,d_type):
    date={
        'name':name,
        'd_type':d_type,
        'race':'狗'       
    }
    if d_type in attack_value:
        date['attack_value']=attack_value[d_type] 
    else:
        date['attack_value']=15     
    if d_type in life_value:
        date['life_value']=life_value[d_type]
    else:
        date['life_value']=150
    return date
#根据狗的品种生成攻击力和生命，并对狗命名

def person(name,age):
    date={
        'name':name,
        'age':age,
        'race':'人类'        
    }
    if age >=18:
        date['attack_value']=80
        date['life_value']=300
    else: 
        date['attack_value']=40 
        date['life_value']=150         
    return date

def attack(do_bite,be_bited):
    be_bited['life_value']-=do_bite['attack_value']
    print(f"{do_bite['race']}{do_bite['name']}攻击了{be_bited['race']}{be_bited['name']},造成了{do_bite['attack_value']}点伤害,{be_bited['name']}还剩下{be_bited['life_value']}点血量")

d1=dog('kurocyan','hashiqi')
d2=dog('sirocyan','zangao')
p1=person('ren',18)
p2=person('ningen',17)
attack(d1,p1)
# print(d1,d2,p1,p2,sep='\n')

# print(p1['life_value'])

# def bite(person_obj):
#     person_obj.life_val-=30

print(d1.__class__.__name__)
