#sk-68e42e2830124a45b6cc22175358f527

import requests
import json
url='https://api.deepseek.com/chat/completions'
#访问网址

messages=[]
headers={'Authorization':'Bearer sk-68e42e2830124a45b6cc22175358f527','Content-Type':'application/json'}
#伪装，访问信息
while True:
    user_question=input('请输入您的问题')
    messages.append({'role':'user','content':user_question})
    data={
        'model':'deepseek-chat',
        'messages':messages
    }



    response=requests.post(url,headers=headers,data=json.dumps(data))
    #get 获取！ post 需要提交信息!(用户名，密码，目的)等,需要提供data，并将其转变为json



    JSON= response.json()
    #将其转变为json格式

    print(JSON['choices'][0]['message']['content'])
    messages.append({'role':'assistant','content':JSON['choices'][0]['message']['content']})

