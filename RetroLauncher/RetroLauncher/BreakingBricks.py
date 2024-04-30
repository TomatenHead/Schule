import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'
import pgzrun
import random
from time import time
import time

game = "pong"
if game == "pong":
    WIDTH = 1550
    HEIGHT = 800
    
    player_y = 100
    ai_y = 500
    
    ball_y = 200
    ball_x = 500
    
    dy = 2
    dx = 2
    
    player_x = 100
    ball_y = 200
    ball_x = 500
    
    dy = 2
    dx = 2
    
    bloecke = [[(40, 100), (190, 100)], [(40, 150), (190, 150)], [(320, 150), (320, 100)], [(440, 150), (440, 100)],[(560, 150), (560, 100)],[(680, 150), (680, 100)],[(800, 150), (800, 100)],[(920, 150), (920, 100)],[(1040, 150), (1040, 100)],[(1160, 150), (1160, 100)],[(1280, 150), (1280, 100)],[(1400, 150), (1400, 100)]]
    A_pressed = False
    D_pressed = False

    score = 0
    
    def draw():
        screen.clear()
        screen.draw.filled_rect(Rect((player_x,600),(100,10)),(255,255,255))
        screen.draw.filled_rect(Rect((ball_x,ball_y),(20,20)),(255,255,255))
        screen.draw.textbox(str(score), Rect((WIDTH/2-25,50),(50,50)))
        for row in bloecke:
            for block in row:
                screen.draw.filled_rect(Rect(block, (100, 30)), (255, 255, 255))
        
    def update():
        global ball_x,score, ball_y, player_x, dy , dx,score
        
        if ball_y >= HEIGHT:
            ball_x = WIDTH/2
            ball_y = HEIGHT/2
            dy = 2
            dx = 0
            player_x = WIDTH/2
            time.sleep(1)
            score -= 2
            
        
        if A_pressed == True:
            player_x -= abs(dy*2)
        if D_pressed == True:
            player_x += abs(dy*2)
        
        if player_x >= WIDTH-100:
            player_x = WIDTH-100
        if player_x <= 0:
            player_x = 0
            
      
            
        ball_y += dy
        ball_x += dx
        
        if ball_y < 0:
            dy = abs(dy)
            dx = random.randint(-4, 4)
        if ball_x >= WIDTH - 20 or ball_x < 0:
            dx = -dx
        if abs(ball_y - 590) <= 5 and abs(ball_x - player_x ) <= 85:
            dy = -abs(dy)
            dx = random.randint(-4, 4)
            
        for row in bloecke:
            for block in row:
                if abs(ball_x - block[0]) <= 50 and abs(ball_y - block[1]) <= 50:
                    row.remove(block)
                    dy = -dy
                    dx = random.randint(-4, 4)
                    score += 1

        bloecke_existieren = False
        for row in bloecke:
            if row:
                bloecke_existieren = True
                break

        if bloecke_existieren == False:
            dy = 0
            dx = 0
            time.sleep(2)
            print("game = Pong")
            file = "//GY100040/Yanise/Desktop/RetroLauncher/main.py"
            os.system(f"python {file}")
            WIDTH = 1
            HEIGHT = 1
        dy += dy*0.0005
        
        
    
    def on_key_down(key):
        global A_pressed, D_pressed
        if key == key.A:
            A_pressed = True 
        if key == key.D:
            D_pressed = True
            
    def on_key_up(key):
        global A_pressed, D_pressed
        if key == key.A:
            A_pressed = False  
        if key == key.D:
            D_pressed = False
            
            
        
    pgzrun.go()