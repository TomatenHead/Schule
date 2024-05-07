import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'
import pgzrun

WIDTH = 1550
HEIGHT = 800

# credits
credits_list = [
    "Game Design: []",
    "Programming: Yanis",
    "Artwork: []",
    "Music: []",
    "Sound Effects: []",
    "Level Design: Notch",
    "Testing: Informatic Class",
    "Special Thanks: Minecraft Community",
    "",
    "Also Try: Zomby slayer",
    "",
    "To Anyone who supported me:",
    "thanks for everything",
    "",
    "please support this indie game",
    "just 1€ makes an impact",
    "seriously, I'm broke..."
]

credits_y = HEIGHT
test = 0
scroll_speed = 1

def draw():
    test = 0
    screen.clear()
    y = credits_y
    for credit in credits_list:
        screen.draw.text(credit, midtop=(WIDTH/2, y), color="white")
        y += 30
        if y < 0:
            test = 1

def update():
    global credits_y
    if keyboard.up or keyboard.w:
        credits_y += 5
    if keyboard.down or keyboard.s:
        credits_y -= 5
    else:
        credits_y -= 1
    print(test)
    if keyboard.down:
        file = "//GY100040/Yanise/Desktop/RetroLauncher/main.py"
        os.system(f"python {file}")
        os.system(f"python main.py")
        quit()
def on_mouse_down():
    file = "//GY100040/Yanise/Desktop/RetroLauncher/main.py"
    os.system(f"python {file}")
    os.system(f"python main.py")
    quit()
    
    
def on_key_down(key):
    if key != keys.DOWN and key != keys.DOWN and key != keys.W and key != keys.S:
        file = "//GY100040/Yanise/Desktop/RetroLauncher/Pong.py"
        os.system(f"python {file}")
        os.system(f"python main.py")
        quit() 
        
pgzrun.go()
