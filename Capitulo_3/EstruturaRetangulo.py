import pygame

def draw_point(text, pos):
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    img = font.render(text, True, WHITE)
    pygame.draw.circle(screen, BLUE, pos, 8)
    screen.blit(img, pos)
    pass

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

running = True
background = GRAY

pygame.init()
screen = pygame.display.set_mode((640, 400))

rect = pygame.Rect(50, 60, 300, 200)
pts = ("topleft", "topright", "bottomleft", "bottomright",
        "midtop", "midright", "midbottom", "midleft", "center")

print(f"x={rect.x}, y={rect.y}, w={rect.w}, h={rect.h}")
print(f"left={rect.left}, top={rect.top}, right={rect.right}, bottom={rect.bottom}")
print(f"center={rect.center}")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, rect, 2)

    for pt in pts:
        # Utiliza code reflection para instanciar as funcoes
        # Lembrando que code deflection deve ser evitado de se 
        # usar no mundo real 
        draw_point(pt, eval('rect.'+pt))

    pygame.display.flip()

pygame.quit()