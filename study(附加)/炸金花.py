import random
import pprint
def player_choice():
    while True:
        try:
            player_num=int(input('请输入要参加的人数:'))
            break
        except ValueError:
            print('请输入人数，也就是阿拉伯数字')
    player_list=[]
    for player_ in range(player_num):
        player_list.append(input(f'第{player_+1}位玩家的名字为：'))
    return player_list
    #玩家选择人数及姓名

def card_generate():
    card_all=[]
    card_all_number=['3','4','5','6','7','8','9','10','J','Q','K','A','2']
    card_all_type=['黑桃','红桃','方片','梅花']
    for card_type in card_all_type:
        for i in card_all_number:
            card_all.append(f'{card_type}{i}')
    return card_all
    #扑克牌生成

def card_distribute(player,card):
    player_card={}    
    for plr in player: 
        card_3=[] 
        for i in range(3):
            x=random.choice(card)
            card_3.append(x)
            card.remove(x)
        player_card[plr]=card_3
    pprint.pprint(player_card)
    #扑克牌分发

player_list=player_choice()
card_all=card_generate()
card_distribute(player_list,card_all)




