import pygame
import math
import phys 



pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

clock = pygame.time.Clock()



r = phys.Object("Rect",10)

rgrav = phys.Force(9.8,(phys.twopi * 3)/4,-1)
rnorm = phys.Force(9.8,phys.twopi/4,-1)
rapp = phys.Force(100,0,1)

r.forces.append(rgrav)
r.forces.append(rnorm)
r.forces.append(rapp)

entities = [r]

r1 = pygame.Rect(0,0,10,10)

run = True
while run:

    pygame.draw.rect(screen, (255,0,0),r1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for entity in entities:
        phys.updatePosition(entity,50)

    clock.tick(50)

    pygame.display.update()


pygame.quit()