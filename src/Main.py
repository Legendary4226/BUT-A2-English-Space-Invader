import pygame
from pygame.locals import *
from interface.EntitiesManager import EntityManager

from game.entities.Ship import Ship
from game.entities import Bullet

pygame.init()

font = pygame.font.SysFont("Arial", 20, bold=False, italic=False)

width = 1280
height = 720
screen = pygame.display.set_mode((width,height))



pygame.display.set_caption('SPACE INVADER')
# imp = pygame.image.load("./img/logo.png").convert()
# btn = pygame.image.load("./img/start.png").convert()
# btn =  pygame.transform.scale(btn,(240,100))   

# screen.blit(imp, (width/7+2  , height/5))
# screen.blit(btn,(width/7+325,height-height/4))

entityManager = EntityManager()

# TESTS

ship = Ship()
ship.setImage("src/img/ship.png", 50, 50)
entityManager.addEntity(ship)
ship._position = [width/2, 9*height/10]

bullets = []

# END TESTS

# MAIN LOOP
launched = True
while launched:
    if len(pygame.event.get(pygame.QUIT)) == 1:
        launched = False

    entityManager.draw(screen)

    for event in pygame.event.get(exclude=pygame.QUIT):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_bullet = Bullet()
                    new_bullet.setImage()
                if event.key == pygame.K_q:
                    ship._speed = -.5
                if event.key == pygame.K_d:
                    ship._speed = .5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q or event.key == pygame.K_d:
                    ship._speed = 0

    pygame.display.flip()
