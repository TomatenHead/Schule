import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '250,100'
import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600

def draw():
    screen.clear()
    screen.draw.textbox("press 1 to play Pong,", Rect((300,200),(200,100)))
    screen.draw.textbox("press 2 to play Brickbreaker", Rect((300,300),(200,100)))
def update():
    print(1)
    
def on_key_down(key):
    if key == key.K_1:
        print("game = Brick")
        file = "//GY100040/Yanise/Desktop/RetroLauncher/Pong.py"
        os.system(f"python {file}")
        quit()
    if key == key.K_2:
        print("game = Brick")
        file = "//GY100040/Yanise/Desktop/RetroLauncher/BreakingBricks.py"
        os.system(f"python {file}")
        quit()
def on_key_up(key):
    pass
    

pgzrun.go()
    

