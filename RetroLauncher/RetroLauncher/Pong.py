import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'
import pygame
import pgzrun
import random
from time import time

WIDTH = 1535
HEIGHT = 790

player_y = 100
ai_y = 500

ball_y = 200
ball_x = 500

dy = 2
dx = 2

W_pressed = False
S_pressed = False

score_player = 0
score_ai = 0

freeze_x = 0
freeze_y = 0
freeze = False
pause = False
end = False

def draw():
    screen.clear()
    screen.draw.filled_rect(Rect((100, ai_y), (10, 100)), (255, 255, 255))
    screen.draw.filled_rect(Rect((WIDTH - 100, player_y), (10, 100)), (255, 255, 255))
    screen.draw.filled_rect(Rect((ball_x, ball_y), (20, 20)), (255, 255, 255))
    screen.draw.filled_rect(Rect((freeze_x, freeze_y), (50, 50)), (0, 0, 255))
    screen.draw.textbox(str(score_ai), Rect((150, 50), (50, 50)))
    screen.draw.textbox(str(score_player), Rect((WIDTH - 200, 50), (50, 50)))
    screen.draw.textbox("zu", Rect((WIDTH / 2 - 50, 30), (50, 50)))
    screen.draw.line((WIDTH / 2 - 25, 80), (WIDTH / 2 - 25, HEIGHT), (255, 255, 255))
    screen.draw.line((WIDTH / 2 - 25, 0), (WIDTH / 2 - 25, 30), (255, 255, 255))
    if pause == True:
        screen.draw.filled_rect(Rect((WIDTH / 2 - 100, HEIGHT / 2 - 75), (50, 200)), (255, 255, 255))
        screen.draw.filled_rect(Rect((WIDTH / 2 + 25, HEIGHT / 2 - 75), (50, 200)), (255, 255, 255))

def update():
    global WIDTH, HEIGHT, ball_x, score_ai, score_player, ball_y, player_y, ai_y, dy, dx, freeze_x, freeze_y, freeze, dxalt, dyalt, end
    if ball_x >= WIDTH:
        score_ai += 1
        ball_x = 500
        ball_y = 200
    elif ball_x <= 0:
        score_player += 1
        ball_x = 500
        ball_y = 200

    if W_pressed == True:
        player_y += abs(dx * 1.2)
    if S_pressed == True:
        player_y -= abs(dx * 1.2)

    if player_y >= HEIGHT - 100:
        player_y = HEIGHT - 100
    if player_y <= 0:
        player_y = 0

    if ai_y >= HEIGHT - 100:
        ai_y = HEIGHT - 100
    if ai_y <= 0:
        ai_y = 0

    if ai_y >= ball_y - 50:
        ai_y -= abs(dx / 1.2)
    elif ai_y <= ball_y + 50:
        ai_y += abs(dx / 1.2)

    ball_y += dy
    ball_x += dx

    if ball_y <= 0 or ball_y >= HEIGHT - 20:
        dy = -dy
    if (ball_x + 20 >= WIDTH - 100 and ball_y + 20 >= player_y and ball_y <= player_y + 100) or (
            ball_x <= 110 and ball_y + 20 >= ai_y and ball_y <= ai_y + 100):
        dx = -dx
        dy = random.randint(-4, 4)
    if (abs(ball_x - freeze_x) <= 10) and (abs(ball_x - freeze_x) <= 10):
        t_0 = time()
        dx = dx / 2
        dy = dy / 2
        freeze_x = 1500
        freeze_y = 1500
        freeze = True

    dx += 0.005
    dy += 0.005
    if not freeze and not pause:
        if random.randint(1, 300) == 1:
            freeze_x = WIDTH / 2
            freeze_y = HEIGHT / 2
            print("freeze")

            freeze = True
        else:
            freeze_x = 1500
            freeze_y = 1500
    if dy != 0 and dx != 0:
        dyalt = dy
        dxalt = dx
    if pause:
        dy = 0
        dx = 0
    else:
        dy = dyalt
        dx = dxalt
    if end == True:
        try:
            with open(file_path):
                os.system(f"python //GY100040/Yanise/Desktop/RetroLauncher/main.py")
        except FileNotFoundError:
            print(f"File not found: //GY100040/Yanise/Desktop/RetroLauncher/main.py. Playing alternative credits.py")
            os.system(f"python credits.py")

def on_key_down(key):
    global W_pressed, S_pressed, pause, end
    if key == keys.ESCAPE:
        os.system("taskkill /IM python.exe /F")
    if key == key.S:
        W_pressed = True
    elif key == key.W:
        S_pressed = True
    if key == key.K_1:
        if pause == False:
            pause = True
        else:
            pause = False
    if key == key.K_2:
        end = True

def on_key_up(key):
    global W_pressed, S_pressed
    if key == key.S:
        W_pressed = False
    if key == key.W:
        S_pressed = False

def on_init():
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    if joystick_count < 1:
        print("PS4 controller not detected. Falling back to keyboard input.")
    else:
        print(f"PS4 controller detected. Found {joystick_count} controller(s).")

pgzrun.go()
