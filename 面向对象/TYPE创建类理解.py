# 静态定义怪物类
class Goblin:
    hp = 50
    attack = 10

# 但玩家升级后需要更强的怪物...
# 动态生成不同强度的怪物
def create_monster(name, level):
    return type(name, (), {
        'hp': 20 * level,
        'attack': 5 * level
    })

# 根据玩家等级生成怪物
player_level = 3
Dragon = create_monster("FireDragon", player_level)
print(type(Dragon))
monster = Dragon()
print(f"怪物血量:{monster.hp}")  # 输出60


# 用户说要三角形的草莓饼干
shape = input("要什么形状? ")  # 用户输入"三角形"
flavor = input("要什么口味? ") # 用户输入"草莓"

# 动态创建饼干模具（类）
CustomCookie = type('CustomCookie', (), {
    'shape': shape,
    'flavor': flavor
})

