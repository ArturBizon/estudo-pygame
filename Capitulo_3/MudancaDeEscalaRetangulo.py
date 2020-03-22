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
comandos = {K_LEFT:(-5,0), K_RIGHT:(5,0), K_UP:(0,-5), K_DOWN:(0,5),
            K_PLUS:(5,5), K_MINUS:(-5,-5), K_KP_PLUS:(5,5), 
            K_KP_MINUS:(-5,-5)}


width, height = SIZE
pygame.init()
screen = pygame.display.set_mode(SIZE)

rectPai = Rect(50, 60, 80, 80)
rectFilho = rectPai.copy()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == KEYDOWN:
            if event.key in comandos:
                valor = comandos[event.key]
                rectFilho.inflate_ip(valor)
    
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLUE, rectPai, 5)
    pygame.draw.rect(screen, GREEN, rectFilho, 5)

    pygame.display.flip()

pygame.quit()