import os
import json
def sava_data(data,file_name):
    with open(file_name,'w',encoding='utf-8') as f1:
            json.dump(data,f1,indent=4)

data={}

file_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'users.json')
with open(file_path,'r',encoding='utf-8') as f:
    data=json.load(f)

while True:  
    user_name=input('用户名：')
    pwd=input('密码：')   
    
    if user_name in data:
        if pwd == data[user_name]['password'] and data[user_name]['attempts_left']>0:
            print(f'登录成功，欢迎您，{user_name}')
            data[user_name]['attempts_left']=3
            sava_data(data,file_path)
            break
        elif pwd!=data[user_name]['password'] and data[user_name]['attempts_left']>1:
            print(f"密码不正确，请重新输入,提醒：三次连续错误会锁定用户，您还剩{data[user_name]['attempts_left']-1}次输入机会")
            data[user_name]['attempts_left']-=1
            sava_data(data,file_path)
            continue
        elif pwd!=data[user_name]['password'] and data[user_name]['attempts_left']==1:
            print('您的用户已被锁定,不能再进行登录，请联系管理员解锁')
            data[user_name]['attempts_left']-=1
            sava_data(data,file_path)         
            continue
        elif data[user_name]['attempts_left']==0:
            print('您的用户已被锁定,不能再进行登录，请联系管理员解锁')
            continue
    else:
        print('用户名不存在')



