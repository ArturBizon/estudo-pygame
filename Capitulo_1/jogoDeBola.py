import pygame
from pygame.locals import *


RED = (255, 0, 0)
GREEN = (0, 255, 0)

size = 640, 320
width, height = size

pygame.init()
screen = pygame.display.set_mode(size)
running = True

imagemBola = "Capitulo_1/bola.jpg"
ball = pygame.image.load(imagemBola)
ball = pygame.transform.scale(ball, (80, 80))
rect = ball.get_rect()
speed = [1, 1]

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]
    
    screen.fill(GREEN)
    pygame.draw.rect(screen, RED, rect, 1) 
    screen.blit(ball, rect)
    
    pygame.display.update()