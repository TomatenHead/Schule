import pgzrun

WIDTH = 800
HEIGHT = 600

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
    "Also Try: Lukas's Game",
    "",
    "To Anyone who supported me:",
    "thanks for everything",
    "",
    "please support this indie game",
    "just 1€ makes an impact",
    "seriously, I'm broke..."
]

credits_y = HEIGHT

scroll_speed = 1

def draw():
    screen.clear()
    y = credits_y
    for credit in credits_list:
        screen.draw.text(credit, midtop=(WIDTH/2, y), color="white")
        y += 30

def update():
    global credits_y
    if keyboard.up:
        credits_y += 5
    if keyboard.down:
        credits_y -= 5
    else:
        credits_y -= 1

pgzrun.go()
