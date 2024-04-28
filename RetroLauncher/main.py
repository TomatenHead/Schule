import os
import sys
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'
import pgzrun
import random
import pygame

def get_screen_dimensions():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = pygame.display.get_surface().get_size()
    pygame.quit()
    return width, height

width, height = get_screen_dimensions()

WIDTH = width-65
HEIGHT = height-110
pygame.font.init()
def draw():
    screen.clear()
    screen.draw.textbox("Press 1 to play Pong", Rect((WIDTH/2 - 100, HEIGHT/2 - 50), (200, 100)), color="white")
    screen.draw.textbox("Press 2 to play Brickbreaker", Rect((WIDTH/2 - 100, HEIGHT/2 + 50), (200, 100)), color="white")


def on_key_down(key):
    if key == keys.K_1:
        print("game = Pong")
        os.system("python Pong.py")
        quit()
    if key == keys.K_2:
        print("game = Brickbreaker")
        os.system("python BreakingBricks.py")
        quit()

pgzrun.go()
