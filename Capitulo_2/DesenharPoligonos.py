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
points =[]
polygons = []
pygame.init()
screen = pygame.display.set_mode((640, 240))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == MOUSEBUTTONDOWN and drawing:
            points.append(event.pos)

        elif event.type == MOUSEMOTION and drawing:
            if len(points) > 0:
                points[-1] = event.pos
        
        elif event.type == KEYDOWN:
            if event.key == K_c:
                drawing = True

            elif event.key == K_f:
                if len(points) > 1:
                    points.pop()
                    polygons.append(points)
                points = []
                drawing = False
    
    screen.fill(background)

    for polygon in polygons:
        pygame.draw.polygon(screen, finishedRectangColor, polygon, 8)

    if  len(points) > 1:
        pygame.draw.lines(screen, drawingRectangColor, True, points, 4)

    pygame.display.update()

pygame.quit()