import pygame
import random

# 初始化游戏
pygame.init()

# 定义颜色
COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 150, 0),
    (0, 0, 255),
    (255, 120, 0),
    (255, 255, 0),
    (180, 0, 255),
    (0, 220, 220)
]

# 定义游戏区域尺寸
WIDTH = 300
HEIGHT = 600
BLOCK_SIZE = 30

# 定义方块形状
SHAPES = [
    [[1, 1, 1, 1]],  # I型
    [[1, 1], [1, 1]],  # O型
    [[1, 1, 1], [0, 1, 0]],  # T型
    [[1, 1, 1], [1, 0, 0]],  # L型
    [[1, 1, 1], [0, 0, 1]],  # J型
    [[1, 1, 0], [0, 1, 1]],  # S型
    [[0, 1, 1], [1, 1, 0]]   # Z型
]

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("俄罗斯方块")
        self.clock = pygame.time.Clock()
        self.board = [[0] * (WIDTH // BLOCK_SIZE) for _ in range(HEIGHT // BLOCK_SIZE)]
        self.score = 0
        self.new_piece()

    def new_piece(self):
        self.current_shape = random.choice(SHAPES)
        self.current_color = random.randint(1, len(COLORS)-1)
        self.x = (len(self.board[0]) - len(self.current_shape[0])) // 2
        self.y = 0

    def check_collision(self):
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    if (self.y + y >= len(self.board) or
                        self.x + x < 0 or self.x + x >= len(self.board[0]) or
                        self.board[self.y + y][self.x + x]):
                        return True
        return False

    def lock_piece(self):
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.y + y][self.x + x] = self.current_color
        self.clear_lines()
        self.new_piece()

    def clear_lines(self):
        lines_cleared = 0
        for y in range(len(self.board)):
            if 0 not in self.board[y]:
                del self.board[y]
                self.board.insert(0, [0] * (WIDTH // BLOCK_SIZE))
                lines_cleared += 1
        self.score += lines_cleared * 10

    def run(self):
        fall_time = 0
        fall_speed = 500  # 下落间隔（毫秒）

        while True:
            self.screen.fill(COLORS[0])
            fall_time += self.clock.get_rawtime()
            self.clock.tick()

            # 自动下落
            if fall_time >= fall_speed:
                self.y += 1
                if self.check_collision():
                    self.y -= 1
                    self.lock_piece()
                fall_time = 0

            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x -= 1
                        if self.check_collision():
                            self.x += 1
                    if event.key == pygame.K_RIGHT:
                        self.x += 1
                        if self.check_collision():
                            self.x -= 1
                    if event.key == pygame.K_DOWN:
                        self.y += 1
                        if self.check_collision():
                            self.y -= 1
                            self.lock_piece()
                    if event.key == pygame.K_UP:  # 旋转
                        self.current_shape = list(zip(*reversed(self.current_shape)))
                        if self.check_collision():
                            self.current_shape = list(zip(*self.current_shape[::-1]))

            # 绘制游戏界面
            for y in range(len(self.board)):
                for x in range(len(self.board[0])):
                    color = COLORS[self.board[y][x]]
                    pygame.draw.rect(self.screen, color, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE-1, BLOCK_SIZE-1))

            # 绘制当前方块
            for y, row in enumerate(self.current_shape):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(self.screen, COLORS[self.current_color],
                                        ((self.x + x)*BLOCK_SIZE, (self.y + y)*BLOCK_SIZE,
                                         BLOCK_SIZE-1, BLOCK_SIZE-1))

            pygame.display.flip()

if __name__ == "__main__":
    game = Tetris()
    game.run()