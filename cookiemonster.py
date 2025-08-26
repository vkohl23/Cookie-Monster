import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CookieMonster")

player_img = pygame.image.load("boy.png")
player_img = pygame.transform.scale(player_img, (40, 40))
player_size = 40

cookie_img = pygame.image.load("cookie.jpg")
cookie_img = pygame.transform.scale(cookie_img, (20, 20))
cookie_size = 20

broccoli_img = pygame.image.load("broccoli.png")
broccoli_img = pygame.transform.scale(broccoli_img, (40, 40))
broccoli_size = 40

player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

cookies = []
for _ in range(20):
    x = random.randint(0, WIDTH - cookie_size)
    y = random.randint(0, HEIGHT - cookie_size)
    cookies.append(pygame.Rect(x, y, cookie_size, cookie_size))

broccolis = []
for _ in range(5):
    x = random.randint(0, WIDTH - broccoli_size)
    y = random.randint(0, HEIGHT - broccoli_size)
    broccolis.append(pygame.Rect(x, y, broccoli_size, broccoli_size))

broccoli_speed = 2
score = 0
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    if player_x < 0: player_x = 0
    if player_x > WIDTH - player_size: player_x = WIDTH - player_size
    if player_y < 0: player_y = 0
    if player_y > HEIGHT - player_size: player_y = HEIGHT - player_size

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    for cookie in cookies[:]:
        win.blit(cookie_img, (cookie.x, cookie.y))
        if player_rect.colliderect(cookie):
            cookies.remove(cookie)
            score += 1

    for broccoli in broccolis:
        dx = player_x - broccoli.x
        dy = player_y - broccoli.y
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist
            broccoli.x += dx * broccoli_speed
            broccoli.y += dy * broccoli_speed

        if broccoli.x < 0: broccoli.x = 0
        if broccoli.x > WIDTH - broccoli_size: broccoli.x = WIDTH - broccoli_size
        if broccoli.y < 0: broccoli.y = 0
        if broccoli.y > HEIGHT - broccoli_size: broccoli.y = HEIGHT - broccoli_size

        win.blit(broccoli_img, (broccoli.x, broccoli.y))
        if player_rect.colliderect(broccoli):
            running = False

    win.blit(player_img, (player_x, player_y))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(score_text, (10, 10))
    pygame.display.update()

pygame.quit()
print(f"Game Over! Your score: {score}")
