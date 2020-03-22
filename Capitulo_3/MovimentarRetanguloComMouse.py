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

SIZE = 600,600
running = True
moving = False
background = GRAY
comandos = {K_LEFT:(-5,0), K_RIGHT:(5,0), K_UP:(0,-5), K_DOWN:(0,5),
            K_PLUS:(5,5), K_MINUS:(-5,-5), K_KP_PLUS:(5,5), 
            K_KP_MINUS:(-5,-5)}


width, height = SIZE
pygame.init()
screen = pygame.display.set_mode(SIZE)

rect = Rect(50, 60, 200, 80)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        
        elif event.type == MOUSEMOTION and moving:
            deslocamentoMouse = event.rel
            rect.move_ip(deslocamentoMouse)
    
    screen.fill(GRAY)
    if moving:
        pygame.draw.rect(screen, RED, rect, 0)
    else:
        pygame.draw.rect(screen, GREEN, rect, 0)

    pygame.display.flip()

pygame.quit()