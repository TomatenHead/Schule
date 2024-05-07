import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 1535
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the players
player_WIDTH = 10
player_HEIGHT = 100
player_SPEED = 5

player1_player = pygame.Rect(50, SCREEN_HEIGHT // 2 - player_HEIGHT // 2, player_WIDTH, player_HEIGHT)
player2_player = pygame.Rect(SCREEN_WIDTH - 50 - player_WIDTH, SCREEN_HEIGHT // 2 - player_HEIGHT // 2, player_WIDTH, player_HEIGHT)

# Define the ball
BALL_SIZE = 15
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 3 * random.choice((1, -1))
ball_speed_y = 3 * random.choice((1, -1))

# Define game variables
score_player1 = 0
score_player2 = 0
FONT_SIZE = 36
font = pygame.font.SysFont(None, FONT_SIZE)

# Main game loop
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Move players with joysticks
    joystick_count = pygame.joystick.get_count()
    if joystick_count > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        player1_player.y += int(joystick.get_axis(1) * player_SPEED)

    # Move players with keyboard (for testing without joysticks)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2_player.y -= player_SPEED
    if keys[pygame.K_DOWN]:
        player2_player.y += player_SPEED

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions with walls
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0:
        score_player2 += 1
        ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    if ball.right >= SCREEN_WIDTH:
        score_player1 += 1
        ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    # Ball collisions with players
    if ball.colliderect(player1_player) or ball.colliderect(player2_player):
        ball_speed_x *= -1
    ball_speed_x = ball_speed_x*1.0005
    ball_speed_y = ball_speed_y*1.0005
    if ball_speed_x >= 7:
        ball_speed_x = 7
    if ball_speed_y >= 7:
        ball_speed_y = 7
        
    #if player2_player.y>=0:
    #    player2_player.y -= player_SPEED
    #if player2_player.y<= SCREEN_HEIGHT + player_SIZE:
    #    player2_player.y += player_SPEED
    #if player1_player.y>=0:
    #    player1_player.y -= player_SPEED
    #if player1_player.y<=SCREEN_HEIGTH + player_SIZE:
    #    player1_player.y += player_SPEED
    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1_player)
    pygame.draw.rect(screen, WHITE, player2_player)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Display scores
    player1_score_text = font.render(str(score_player1), True, WHITE)
    player2_score_text = font.render(str(score_player2), True, WHITE)
    screen.blit(player1_score_text, (SCREEN_WIDTH // 4, 20))
    screen.blit(player2_score_text, (3 * SCREEN_WIDTH // 4 - FONT_SIZE // 2, 20))

    pygame.display.flip()

pygame.quit()
