import pygame
import math
import phys 



pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

clock = pygame.time.Clock()



r = phys.Object("Rect",10)

#rgrav = phys.Force(9.8,(phys.twopi * 3)/4,-1)
#rnorm = phys.Force(9.8,phys.twopi/4,-1)
rapp = phys.Force(50,phys.twopi/4,1)
rapp2 = phys.Force(50,3*phys.twopi/4,1)

#r.forces.append(rgrav)
#r.forces.append(rnorm)
r.forces.append(rapp)
r.forces.append(rapp2)

entities = [r]

r1 = pygame.Rect(400,300,10,10)

objs = [r1]
run = True
frame = 0

while run:
    screen.fill((0, 0, 0)) 
    pygame.draw.rect(screen, (255,0,0),r1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for entity in entities:
        phys.updateAccel(entity,50)
        entity.x, entity.y = phys.newCoords(entity, 50,objs[entities.index(entity)].x, objs[entities.index(entity)].y )
        objs[entities.index(entity)].x  = entity.x
        objs[entities.index(entity)].y = entity.y 

        

    clock.tick(50)

    font = pygame.font.SysFont(None, 48)

    frame +=1
    text_surface = font.render('Frame:' +str(frame), True, (255, 255, 255))

    screen.blit(text_surface, (15, 15))

    pygame.display.update()


pygame.quit()