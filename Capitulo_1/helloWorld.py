import pygame 

#Cores
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

running = True
background = GRAY

pygame.init()

screen = pygame.display.set_mode((640, 240))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            
            elif event.key == pygame.K_b:
                background = BLUE
            
            elif event.key == pygame.K_g:
                background = GREEN
    
    screen.fill(background)
    pygame.display.update()

pygame.quit()