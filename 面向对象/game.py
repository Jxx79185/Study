import pygame
import random

pygame.init()

# 窗口大小
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("躲避球游戏")

clock = pygame.time.Clock()

# 玩家
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - 80
player_speed = 7

# 敌人
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = 0
enemy_speed = 5

score = 0

font = pygame.font.SysFont(None, 36)

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 键盘输入
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # 防止出界
    if player_x < 0:
        player_x = 0

    if player_x > WIDTH - player_size:
        player_x = WIDTH - player_size

    # 敌人下降
    enemy_y += enemy_speed

    # 敌人重新生成
    if enemy_y > HEIGHT:
        enemy_y = 0
        enemy_x = random.randint(0, WIDTH - enemy_size)
        score += 1

    # 碰撞检测
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    if player_rect.colliderect(enemy_rect):
        print("游戏结束")
        running = False

    # 画面
    screen.fill((0, 0, 0))

    # 玩家
    pygame.draw.rect(
        screen,
        (0, 255, 0),
        (player_x, player_y, player_size, player_size)
    )

    # 敌人
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (enemy_x, enemy_y, enemy_size, enemy_size)
    )

    # 分数
    score_text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()