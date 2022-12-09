import pygame
from pygame.locals import *
from interface.EntitiesManager import EntityManager

pygame.init()

font = pygame.font.SysFont("Arial", 20, bold=False, italic=False)

width = 1280
height = 920
screen = pygame.display.set_mode((width,height))



# pygame.display.set_caption('SPACE INVADER')
# imp = pygame.image.load("./img/logo.png").convert()
# btn = pygame.image.load("./img/start.png").convert()
# btn =  pygame.transform.scale(btn,(240,100))   

# screen.blit(imp, (width/7+2,height/5))
# screen.blit(btn,(width/7+325,height-height/4))
# pygame.display.flip()

entityManager = EntityManager()

# TESTS



# END TESTS

# MAIN LOOP
launched = True
while launched:
    if pygame.event.get(pygame.QUIT).type != None:
        launched = False

    entityManager.draw()
    entityManager.event(pygame.event.get())
