import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'
import pgzrun
from random import randint

WIDTH = 1535
HEIGHT = 790
GRID_SIZE = 37

snake = [(GRID_SIZE, GRID_SIZE)]
direction = 'RIGHT'
food = (randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE, randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
game_over = False
speed = 50  
frame_count = 0  


def draw():
    screen.clear()
    
    if game_over:
        screen.fill((100,20,10))
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2), fontsize=350, color='red')
    else:
        screen.fill((30,140,20))

        for segment in snake:
            screen.draw.filled_rect(Rect(segment, (GRID_SIZE, GRID_SIZE)), 'yellow')

        screen.draw.filled_rect(Rect(food, (GRID_SIZE, GRID_SIZE)), 'red')



def update():
    global snake, direction, food, game_over, frame_count

    
    
    frame_count += 1
    if frame_count % (30 // (speed // 10)) != 0:  
        return

    head_x, head_y = snake[0]

    if direction == 'RIGHT':
        head_x += GRID_SIZE
    elif direction == 'LEFT':
        head_x -= GRID_SIZE
    elif direction == 'UP':
        head_y -= GRID_SIZE
    elif direction == 'DOWN':
        head_y += GRID_SIZE

    new_head = (head_x, head_y)

    if new_head in snake or head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        file = "//GY100040/Yanise/Desktop/RetroLauncher/main.py"
        try:
            with open(file):
                os.system(f"python {file}")
        except FileNotFoundError:
            print(f"File not found: //GY100040/Yanise/Desktop/RetroLauncher/main.py. Playing alternative credits.py")
            os.system(f"python credits.py")

    snake.insert(0, new_head)

    if new_head == food:
        food = (randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE, randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
    else:
        snake.pop()

def on_key_down(key):
    global direction
    if key == keys.ESCAPE:
        os.system("taskkill /IM python.exe /F")

    if (key == keys.RIGHT or key == keys.D) and direction != 'LEFT':
        direction = 'RIGHT'
    elif (key == keys.LEFT or key == keys.A) and direction != 'RIGHT':
        direction = 'LEFT'
    elif (key == keys.UP or key == keys.W) and direction != 'DOWN':
        direction = 'UP'
    elif (key == keys.DOWN or key == keys.S) and direction != 'UP':
        direction = 'DOWN'


pgzrun.go()
