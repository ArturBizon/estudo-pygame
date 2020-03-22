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
screenCenter = width//2, height//2
pygame.init()
screen = pygame.display.set_mode(SIZE)
img0 = pygame.image.load(imagePath)
# Torna a imagem mais leve para o render
img0.convert()
scale = 1
angle = 0

rect0 = img0.get_rect()
pygame.draw.rect(img0, GREEN, rect0, 2)


img = img0
rect = img.get_rect()
rect.center = screenCenter

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
        elif event.type == KEYDOWN:
            if event.key == K_r:
                if event.mod & KMOD_SHIFT:
                    angle -= 10
                else:
                    angle += 10
                img = pygame.transform.rotozoom(img0, angle, scale)
            
            elif event.key == K_s:
                if event.mod & KMOD_SHIFT:
                    scale /= 1.1
                else:
                    scale *= 1.1
                img = pygame.transform.rotozoom(img0, angle, scale)
            
            elif event.key == K_h:
                img = pygame.transform.flip(img, True, False)

            elif event.key == K_v:
                img = pygame.transform.flip(img, False, True)
            
            elif event.key == K_o:
                img = img0 
                scale = 1
                angle = 0

            rect = img.get_rect()
            rect.center = screenCenter

    
    screen.fill(GRAY)
    screen.blit(img, rect)
    if moving:
        pygame.draw.rect(screen, RED, rect, 4)
    else:
        pygame.draw.rect(screen, GREEN, rect, 4)

    pygame.display.update()

pygame.quit()