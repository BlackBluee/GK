import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Z")

BIALY = (255, 255, 255)
CZERWONY = (255, 0, 0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill(BIALY)
    pygame.draw.line(win, CZERWONY, (200, 200), (400, 200), 10)
    pygame.draw.line(win, CZERWONY, (400, 200), (200, 400), 13)
    pygame.draw.line(win, CZERWONY, (200, 400), (400, 400), 10)
    
    pygame.display.update()