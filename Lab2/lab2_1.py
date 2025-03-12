import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Transformacje")

BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)
NIEBIESKI = (0, 0, 255)

def get_octagon_vertices(cx, cy, radius):
    return [(cx + radius * math.cos(2 * math.pi * i / 8),
             cy + radius * math.sin(2 * math.pi * i / 8)) for i in range(8)]

def translate(vertices, dx, dy):
    return [(x + dx, y + dy) for x, y in vertices]

def scale(vertices, sx, sy, center):
    cx, cy = center
    return [(cx + (x - cx) * sx, cy + (y - cy) * sy) for x, y in vertices]

def rotate(vertices, angle_deg, center):
    angle_rad = math.radians(angle_deg)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    cx, cy = center
    return [(cx + (x - cx) * cos_a - (y - cy) * sin_a,
             cy + (x - cx) * sin_a + (y - cy) * cos_a) for x, y in vertices]

def shear(vertices, shx=0, shy=0, center=(0, 0)):
    cx, cy = center
    return [(cx + (x - cx) + shx * (y - cy),
             cy + (y - cy) + shy * (x - cx)) for x, y in vertices]

def draw_polygon(win, vertices, edges_color=NIEBIESKI):
    win.fill(BIALY)
    pygame.draw.polygon(win, edges_color, vertices)
    pygame.display.flip()


cx, cy = 300, 300
radius = 150
vertices = get_octagon_vertices(cx, cy, radius)
original_vertices = vertices[:]

draw_polygon(win, vertices)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            v = vertices[:]  

            if event.key == pygame.K_0:
                v = original_vertices[:]  

            elif event.key == pygame.K_1:
                v = scale(v, 0.2, 0.2, (cx, cy))

            elif event.key == pygame.K_2:
                v = rotate(v, 20, (cx, cy))

            elif event.key == pygame.K_3:
                v = scale(v, -0.2, -0.6, (cx, cy))

            elif event.key == pygame.K_4:
                v = shear(v, shx=0.5, center=(cx, cy))

            elif event.key == pygame.K_5:
                v = scale(v, 1, 0.5, (cx, cy))
                v = translate(v, 0, -200)

            elif event.key == pygame.K_6:
                v = scale(v, 1.5, 1.5, (cx, cy))
                v = rotate(v, 90, (cx, cy))
                v = shear(v, shx=0.5, center=(cx, cy))

            elif event.key == pygame.K_7:
                v = scale(v, 0.2, -0.6, (cx, cy))

            elif event.key == pygame.K_8:
                v = scale(v, 1, 0.5, (cx, cy))
                v = rotate(v, 20, (cx, cy))
                v = translate(v, -80, 80)

            elif event.key == pygame.K_9:
                v = rotate(v, 180, (cx, cy))
                v = shear(v, shx=0.5, center=(cx, cy))
                v = translate(v, 120, 0)

            vertices = v
            draw_polygon(win, vertices)

pygame.quit()
