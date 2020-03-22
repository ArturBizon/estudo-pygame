import time

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
moveSpeed = [2,2]
fps = 500
sleepTime = 1 / fps

width, height = SIZE
pygame.init()
screen = pygame.display.set_mode(SIZE)

rect = Rect(50, 60, 200, 80)


while running:
    time.sleep(sleepTime)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    if rect.right > width-1:
        moveSpeed[0] *= -1
    if rect.left < 0:
        moveSpeed[0] *= -1
    if rect.top < 0:
        moveSpeed[1] *= -1
    if rect.bottom > height-1:
        moveSpeed[1] *= -1
    
    rect.move_ip(moveSpeed)
    
    screen.fill(BLACK)
    pygame.draw.rect(screen, CYAN, rect, 0)

    pygame.display.flip()

pygame.quit()