import os
import sys
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'
import pygame,  threading

pygame.init()

# Screen and font
screen = pygame.display.set_mode((1535, 790))
pygame.display.set_caption("Loading Bar!")

FONT = pygame.font.SysFont("Roboto", 100)

# Clock
CLOCK = pygame.time.Clock()

# Work
WORK = 10000000

# Loading BG
LOADING_BG = pygame.image.load("Loading Bar Background.png")
LOADING_BG_RECT = LOADING_BG.get_rect(center=(767, 395))

# Loading Bar and variables
loading_bar = pygame.image.load("Loading Bar.png")
loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
loading_finished = False
loading_progress = 0
loading_bar_width = 8

def doWork():
	# Do some math WORK amount times
	global loading_finished, loading_progress

	for i in range(WORK):
		math_equation = 523687 / 789456 * 89456
		loading_progress = i 

	loading_finished = True

# Finished text
finished = FONT.render("Done!", True, "white")
finished_rect = finished.get_rect(center=(767, 395))

# Thread
threading.Thread(target=doWork).start()
t = 0
# Game loop
while True:
    
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type != pygame.QUIT:
			if t == 120:
                pygame.quit()
                sys.exit()
            else:
                t+=1

	screen.fill("#0d0e2e")

	loading_bar_width = loading_progress / WORK * 720

	loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 150))
	loading_bar_rect = loading_bar.get_rect(midleft=(405, 395))

	screen.blit(LOADING_BG, LOADING_BG_RECT)
	screen.blit(loading_bar, loading_bar_rect)

	pygame.display.update()
    
    
	CLOCK.tick(60)
