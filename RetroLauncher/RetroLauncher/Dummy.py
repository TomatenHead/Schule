import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'
import pgzrun

WIDTH = 1535
HEIGHT = 790

def draw():
    screen.clear()
    screen.draw.text("Game is getting programmed, nothing to see here!", center=(WIDTH/2, HEIGHT-HEIGHT/4), color="white", fontsize=60)
    screen.draw.text("Comming soon!!!", center=(WIDTH/2, HEIGHT/3), color="Yellow", fontsize=200, angle = 12)

pgzrun.go()
