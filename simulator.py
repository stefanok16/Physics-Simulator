import pygame
import math
import phys 

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

clock = pygame.time.Clock()

r = pygame.Rect(300,250,10,10)

run = True
while run:

    pygame.draw.rect(screen, (255,0,0),r)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    pygame.display.update()
    clock.tick(50)


pygame.quit()