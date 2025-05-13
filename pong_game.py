import pygame
import sys

pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Ball properties
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
ball_speed_x = 7 * (-1 if pygame.time.get_ticks() % 2 == 0 else 1)
ball_speed_y = 7 * (-1 if pygame.time.get_ticks() % 2 == 0 else 1)

# Paddle properties
paddle_width = 10
paddle_height = 140
player = pygame.Rect(screen_width - 20, screen_height/2 - paddle_height/2, paddle_width, paddle_height)
player_speed = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_DOWN:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Ball collision with player
    if ball.colliderect(player):
        ball_speed_x *= -1

    # Player movement
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

    # Drawing
    screen.fill(black)
    pygame.draw.rect(screen, white, player)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (screen_width/2, 0), (screen_width/2, screen_height))

    pygame.display.flip()
    pygame.time.Clock().tick(60)