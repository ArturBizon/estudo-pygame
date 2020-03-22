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
imagePath = "Capitulo_4/python.png"
running = True
moving = False
background = GRAY



width, height = SIZE
pygame.init()
screen = pygame.display.set_mode(SIZE)
img = pygame.image.load(imagePath)
# Torna a imagem mais leve para o render
img.convert()

rect = img.get_rect()
rect.center = width//2, height//2



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
    screen.blit(img, rect)
    if moving:
        pygame.draw.rect(screen, RED, rect, 4)
    else:
        pygame.draw.rect(screen, GREEN, rect, 4)

    pygame.display.update()

pygame.quit()