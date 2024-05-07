import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'
import pgzrun

WIDTH = 1550
HEIGHT = 800

def draw():
    screen.clear()
    screen.draw.text("Game is getting programmed, nothing to see here", center=(WIDTH/2, HEIGHT/2), color="white", fontsize=60)

pgzrun.go()