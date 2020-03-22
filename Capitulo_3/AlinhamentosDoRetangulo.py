import pygame
from pygame.rect import *
from pygame.locals import *

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

SIZE = 500, 200
running = True
background = GRAY

width, height = SIZE
pygame.init()
screen = pygame.display.set_mode(SIZE)

rect = Rect(50, 60, 200, 80)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == KEYDOWN:
            #Alinha para esquerda
            if event.key == K_l:
                rect.left = 0
            #Alinha com o centro da largura
            elif event.key == K_c:
                rect.centerx = width//2
            #Alinha com a direita
            elif event.key == K_r:
                rect.right = width       
            #Alinha com o topo
            elif event.key == K_t:
                rect.top = 0
            #Alinha com o centro da altura
            elif event.key == K_m:
                rect.centery = height//2
            #Alinha com a base
            elif event.key == K_b:
                rect.bottom = height
    
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLUE, rect, 0)

    pygame.display.flip()

pygame.quit()