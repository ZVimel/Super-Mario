python
import pygame
import random# 初始化游戏
pygame.init()# 设置游戏窗口大小
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Mario")# 加载玛丽图片
mario_image = pygame.image.load("mario.png")
mario_width, mario_height = 50, 50
mario_x, mario_y = screen_width // 2, screen_height - mario_height# 加载敌人图片
enemy_image = pygame.image.load("enemy.png")
enemy_width, enemy_height = 50, 50
enemy_x, enemy_y = random.randint(0, screen_width - enemy_width), 0
enemy_speed = 5# 游戏主循环
running = True
while running:
    screen.fill((0, 0, 0))  # 清空屏幕    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and mario_x > 0:
        mario_x -= 5
    if keys[pygame.K_RIGHT] and mario_x < screen_width - mario_width:
        mario_x += 5    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = 0    # 碰撞检测
    if mario_x < enemy_x + enemy_width and mario_x + mario_width > enemy_x and mario_y < enemy_y + enemy_height and mario_y + mario_height > enemy_y:
        running = False    screen.blit(mario_image, (mario_x, mario_y))
    screen.blit(enemy_image, (enemy_x, enemy_y))    pygame.display.update()# 游戏结束
pygame.quit()
