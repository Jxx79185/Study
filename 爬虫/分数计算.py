a=int(input('请输入a队的实力：'))
b=int(input('请输入b队的实力：'))
c=int(input('请输入c队的实力：'))
d=int(input('请输入d队的实力：'))

def score(team0,team1,team2,team3):
        team=[team0,team1,team2,team3]
        point_all=0
        for i in range(1,4):
            if team[0]>team[i]:
                point=3
            elif team[0]==team[i]:
                point=1
            elif team[0]<team[i]:
                point=0  
            point_all+=point
        return point_all
#得分函数 


while True:
    i=input('请输入你要计算得分的队伍:')
    if i == 'a':
        score(a,b,c,d)
        print(f'a队能得到的总积分为：{score(a,b,c,d)}')
    elif i=='b':
        score(b,c,d,a)
        print(f'b队能得到的总积分为：{score(b,c,d,a)}')
    elif i=='c':
        score(c,d,a,b)
        print(f'c队能得到的总积分为：{score(c,d,a,b)}')
    elif i=='d':
        score(d,a,b,c)
        print(f'd队能得到的总积分为：{score(d,a,b,c)}')
    elif i=='q':
        print('谢谢使用积分软件')
        break
#用户操作
        



        
