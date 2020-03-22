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
background = GRAY
comandos = {K_LEFT:(-5,0), K_RIGHT:(5,0), K_UP:(0,-5), K_DOWN:(0,5),
            K_PLUS:(5,5), K_MINUS:(-5,-5), K_KP_PLUS:(5,5), 
            K_KP_MINUS:(-5,-5)}


width, height = SIZE
pygame.init()
screen = pygame.display.set_mode(SIZE)

r0 = Rect(50, 60, 200, 80)
r1 = Rect(100, 20, 100, 140)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == KEYDOWN:
            if event.key in comandos:
                r1.move_ip(comandos[event.key])
    
    clip = r0.clip(r1)
    union = r0.union(r1)
    screen.fill(GRAY)
    pygame.draw.rect(screen, YELLOW, union, 0)
    pygame.draw.rect(screen, GREEN, clip, 0)
    pygame.draw.rect(screen, BLUE, r0, 4)
    pygame.draw.rect(screen, RED, r1, 4)

    pygame.display.flip()

pygame.quit()