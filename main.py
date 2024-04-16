import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '250,100'
import pgzrun
import random
game = "pong"
if game == "pong":
    WIDTH = 1200
    HEIGHT = 600
    
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
    
    def draw():
        screen.clear()
        screen.draw.filled_rect(Rect((100,ai_y),(10,100)),(255,255,255))
        screen.draw.filled_rect(Rect((WIDTH-100,player_y),(10,100)),(255,255,255))
        screen.draw.filled_rect(Rect((ball_x,ball_y),(20,20)),(255,255,255))
        screen.draw.textbox(str(score_ai), Rect((150,50),(50,50)))
        screen.draw.textbox(str(score_player), Rect((WIDTH-200,50),(50,50)))
        screen.draw.textbox("zu", Rect((WIDTH/2-50,30),(50,50)))
        screen.draw.line((WIDTH/2-25,80), (WIDTH/2-25,HEIGHT), (255,255,255))
        screen.draw.line((WIDTH/2-25,0), (WIDTH/2-25,30), (255,255,255))
        
    def update():
        global ball_x, score_ai,score_player, ball_y, player_y, ai_y, dy , dx
        if ball_x >= WIDTH:
            score_ai += 1
            ball_x = 500
            ball_y = 200
        elif ball_x <= 0:
            score_player += 1
            ball_x = 500
            ball_y = 200
        
        if W_pressed == True:
            player_y += 3
        if S_pressed == True:
            player_y -= 3
        
        if player_y >= HEIGHT-100:
            player_y = HEIGHT-100
        if player_y <= 0:
            player_y = 0
            
        if ai_y >= HEIGHT-100:
            ai_y = HEIGHT-100
        if ai_y <= 0:
            ai_y = 0
            
        if ai_y >= ball_y-50:
            ai_y -= 1
        elif ai_y <= ball_y+50:
            ai_y += 1
            
        ball_y += dy
        ball_x += dx
        
        if ball_y <= 0 or ball_y >= HEIGHT - 20:
            dy = -dy
        if (ball_x + 20 >= WIDTH - 100 and ball_y + 20 >= player_y and ball_y <= player_y + 100) or (ball_x <= 110 and ball_y + 20 >= ai_y and ball_y <= ai_y + 100):
            dx = -dx
            dy = random.randint(-4,4)
            
        dx += dx*0.001
        
        
    
    def on_key_down(key):
        global W_pressed, S_pressed
        if key == key.S:
            W_pressed = True 
        elif key == key.W:
            S_pressed = True
            
    def on_key_up(key):
        global W_pressed, S_pressed
        if key == key.S:
            W_pressed = False  
        if key == key.W:
            S_pressed = False
            
        
    pgzrun.go()