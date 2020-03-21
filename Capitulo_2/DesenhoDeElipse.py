import pygame

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
    
    screen.fill(background)
    ##pygame.draw.rect(screen, RED, (xInitialPosition, YInitialPosition, Width, height),(BorderWidth=0))
    pygame.draw.ellipse(screen, RED, (50, 20, 160, 100))
    pygame.draw.ellipse(screen, GREEN, (100, 60, 160, 100))
    pygame.draw.ellipse(screen, BLUE, (150, 100, 160, 100))
    
    pygame.draw.ellipse(screen, RED, (350, 20, 160, 100), 1)
    pygame.draw.ellipse(screen, GREEN, (400, 60, 160, 100), 4)
    pygame.draw.ellipse(screen, BLUE, (450, 100, 160, 100), 8)
    
    pygame.display.update()

pygame.quit()