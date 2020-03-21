import pygame
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

start = (0, 0,)
end = (0,0,)
size = (0, 0,)
drawing = False
running = True
background = GRAY
finishedRectangColor = BLACK
drawingRectangColor = BLUE
rectangs = []

pygame.init()
screen = pygame.display.set_mode((640, 240))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos 
            size = (0, 0,)
            drawing = True
        elif event.type == MOUSEBUTTONUP:
            size = (end[0] - start[0], end[1] - start[1])
            rect = pygame.Rect(start, size)
            rectangs.append(rect)
            start = (0, 0,)
            end = (0,0,)
            drawing = False
        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = (end[0] - start[0], end[1] - start[1])
    
    screen.fill(background)

    for rect in rectangs:
        pygame.draw.rect(screen, finishedRectangColor, rect, 8)

    if drawing:
        pygame.draw.rect(screen, drawingRectangColor, (start, size), 0)

    pygame.display.update()

pygame.quit()