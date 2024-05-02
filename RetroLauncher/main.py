Here's the complete code with the modified `draw_pixelated_text()` function:

```python
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'
import pgzrun
from random import randint

# Define box color and border size
BOX_COLOR = "white"
BORDER_COLOR = "black"
BORDER_SIZE = 5

WIDTH = 1535
HEIGHT = 790
message = [
    "also play Zombie Slayer",
    "Insert coin to continue...",
    "Get ready player one!",
    "Prepare for pixelated adventures!",
    "Level up your nostalgia!",
    "Press start and enter the retro realm!",
    "Loading retro goodness...",
    "Retro gaming, timeless fun!",
    "Brace yourself for classic gaming!",
    "Retro vibes loading...",
    "Dust off your controllers, it's retro time!",
    "Welcome to the world of pixels!",
    "Relive the classics in 8-bit glory!",
    "Get set for a blast from the past!"
]

random_index = randint(0, len(message) - 1)

alternator = 0
alternating_speed = 1

FONT_WIDTH = 8  # Width of each character in pixels

def draw_pixelated_text(text, position, color="white"):
    x, y = position
    for char in text:
        if char == " ":
            x += FONT_WIDTH  # Move cursor for space
            continue
        for i in range(len(MINECRAFT_FONT[char])):
            row = MINECRAFT_FONT[char][i]
            for j in range(len(row)):
                pixel = row[j]
                if pixel:  # Draw only if the pixel is 1
                    screen.draw.filled_rect(Rect((x + j*2, y + i*2), (2, 2)), color)
        x += FONT_WIDTH + 2  # Move cursor for next character

MINECRAFT_FONT = {
    "R": [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 1, 0],
    ],
    "e": [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
    ],
    "t": [
        [1, 1, 1],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ],
    "r": [
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
        [1, 0, 1],
    ],
    "o": [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
    ],
}

def draw():
    global alternator, alternating_speed 
    screen.clear()
    screen.fill((50,50,50))
    
    # Main text
    draw_pixelated_text("RetroLauncher", (WIDTH/2, 100), color="white")
    message_length = len(message[random_index])
    if message_length > 20:
        draw_pixelated_text(message[random_index], (WIDTH/2+350, 180), color=(194, 218, 180))
    else:
        draw_pixelated_text(message[random_index], (WIDTH/2+350, 180), color=(194, 218, 180))
    
    # Buttons (unchanged)
    button_close_x = WIDTH/2 - 450
    button_close_y = HEIGHT - 100
    screen.draw.filled_rect(Rect((button_close_x, button_close_y), (200, 100)), BOX_COLOR)
    screen.draw.rect(Rect((button_close_x, button_close_y), (200, 100)), BORDER_COLOR)
    screen.draw.textbox("Close Game", Rect((button_close_x, button_close_y), (200, 100)), color=BORDER_COLOR)
    
    button_credits_x = WIDTH/2 + 250
    button_credits_y = HEIGHT - 100
    screen.draw.filled_rect(Rect((button_credits_x, button_credits_y), (200, 100)), BOX_COLOR)
    screen.draw.rect(Rect((button_credits_x, button_credits_y), (200, 100)), BORDER_COLOR)
    screen.draw.textbox("Credits", Rect((button_credits_x, button_credits_y), (200, 100)), color=BORDER_COLOR)
    
    button_game1_x = WIDTH/2 - 450
    button_game1_y = HEIGHT/2 - 50
    screen.draw.filled_rect(Rect((button_game1_x, button_game1_y), (200, 100)), BOX_COLOR)
    screen.draw.rect(Rect((button_game1_x, button_game1_y), (200, 100)), BORDER_COLOR)
    screen.draw.textbox("BrickBreaker", Rect((button_game1_x, button_game1_y), (200, 100)), color=BORDER_COLOR)
    
    button_game2_x = WIDTH/2 + 250
    button_game2_y = HEIGHT/2 - 50
    screen.draw.filled_rect(Rect((button_game2_x, button_game2_y), (200, 100)), BOX_COLOR)
    screen.draw.rect(Rect((button_game2_x, button_game2_y), (200, 100)), BORDER_COLOR)
    screen.draw.textbox("Pong", Rect((button_game2_x, button_game2_y), (200, 100)), color=BORDER_COLOR)
    
    button_game3_x = WIDTH/2 - 450
    button_game3_y = HEIGHT/2 + 150
    screen.draw.filled_rect(Rect((button_game3_x, button_game3_y), (200, 100)), BOX_COLOR)
    screen.draw.rect(Rect((button_game3_x, button_game3_y), (200, 100)), BORDER_COLOR)
    screen.draw.textbox("Game 3", Rect((button_game3_x, button_game3_y), (200, 100)), color=BORDER_COLOR)
    
    button_game4_x = WIDTH/2 + 250
    button_game4_y = HEIGHT/2 + 150
    screen.draw.filled_rect(Rect((button_game4_x, button_game4_y), (200, 100)), BOX_COLOR)
    screen.draw.rect(Rect((button_game4_x, button_game4_y), (

200, 100)), BORDER_COLOR)
    screen.draw.textbox("Game 4", Rect((button_game4_x, button_game4_y), (200, 100)), color=BORDER_COLOR)

def update():
    global alternator, alternating_speed
    if abs(alternator) >= 30:
        alternating_speed = -alternating_speed
    alternator += alternating_speed

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        if WIDTH/2 - 150 <= pos[0] <= WIDTH/2 + 50 and HEIGHT - 100 <= pos[1] <= HEIGHT:
            close_game()
        elif WIDTH/2 + 250 <= pos[0] <= WIDTH/2 + 450 and HEIGHT - 100 <= pos[1] <= HEIGHT:
            show_credits()
        elif WIDTH/2 - 450 <= pos[0] <= WIDTH/2 - 250 and HEIGHT/2 - 50 <= pos[1] <= HEIGHT/2 + 50:
            play_game1()
        elif WIDTH/2 + 250 <= pos[0] <= WIDTH/2 + 450 and HEIGHT/2 - 50 <= pos[1] <= HEIGHT/2 + 50:
            play_game2()
        elif WIDTH/2 - 450 <= pos[0] <= WIDTH/2 - 250 and HEIGHT/2 + 150 <= pos[1] <= HEIGHT/2 + 250:
            play_game3()
        elif WIDTH/2 + 250 <= pos[0] <= WIDTH/2 + 450 and HEIGHT/2 + 150 <= pos[1] <= HEIGHT/2 + 250:
            play_game4()

def close_game():
    print("Closing game...")
    quit()
    
def show_credits():
    print("Showing credits...")
    print("game = credits")
    file_path = "//GY100040/Yanise/Desktop/RetroLauncher/credits.py"
    try:
        with open(file_path):
            os.system(f"python {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}. Playing alternative credits.py")
        os.system(f"python credits.py")
    quit()
    
def play_game1():
    print("Starting Game 1...")
    print("game = Brick")
    file_path = "//GY100040/Yanise/Desktop/RetroLauncher/BreakingBricks.py"
    try:
        with open(file_path):
            os.system(f"python {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}. Playing alternative Brickbreaker.py")
        os.system(f"python BreakingBricks.py")
    quit()

def play_game2():
    print("Starting Game 2...")
    print("game = Pong")
    file_path = "//GY100040/Yanise/Desktop/RetroLauncher/Pong.py"
    try:
        with open(file_path):
            os.system(f"python {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}. Playing alternative Pong.py")
        os.system(f"python Pong.py")
    quit()

def play_game3():
    print("Starting Game 3...")
    print("game = Pong")
    file_path = "//GY100040/Yanise/Desktop/RetroLauncher/Dummy.py"
    try:
        with open(file_path):
            os.system(f"python {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}. Playing alternative Dummy.py")
        os.system(f"python Dummy.py")

def play_game4():
    print("Starting Game 4...")
    print("game = Pong")
    file_path = "//GY100040/Yanise/Desktop/RetroLauncher/Dummy.py"
    try:
        with open(file_path):
            os.system(f"python {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}. Playing alternative Dummy.py")
        os.system(f"python Dummy.py")

pgzrun.go()
```