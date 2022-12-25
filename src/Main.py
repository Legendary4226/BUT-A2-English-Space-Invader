import pygame
from pygame.locals import *
from interface.EntitiesManager import EntityManager

from game.entities.ships.players.Player import Player
from game.entities.Bullet import Bullet
from game.WaveGenerator import WaveGenerator



### Init Global Variables

pygame.init()
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 20, bold=False, italic=False)

width = 720
height = 720
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('SPACE INVADER')


### Init Game Variables

entityManager = EntityManager()

player = Player()
player.setImage("img/ship.png", 50, 50)
entityManager.addEntity(player)
player._position = [width/2, 9*height/10]

playerBullets = []

waveGenerator = WaveGenerator(player, entityManager, screen)


### Sensor

from sense_hat import SenseHat
sense = SenseHat()

#accelerometer = sense.get_accelerometer_raw()


def calculateVelocity():
    if(accelerometer<0):
        #we go to the left
        if(accelerometer<-0.7):
            return -5
        elif(accelerometer<-0.5):
            return -3
        elif(accelerometer<-0.3):
            return -1
        else:
            return 0
    if(accelerometer>0):
        #we go to the right
        if(accelerometer>0.7):
            return 5
        elif(accelerometer>0.5):
            return 3
        elif(accelerometer>0.3):
            return 1
        else:
            return 0
    return 0





### MAIN LOOP
launched = True
while launched:
    screen.fill((0,0,0))

    if len(pygame.event.get(pygame.QUIT)) == 1:
        launched = False

    entityManager.draw(screen)
    waveGenerator.update()

    for event in pygame.event.get(exclude=pygame.QUIT):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    player._speed = -4
                if event.key == pygame.K_d:
                    player._speed = 4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q or event.key == pygame.K_d:
                    player._speed = 0
                if event.key == pygame.K_SPACE:
                    pos = player._position.copy()
                    pos[0] += 16
                    pos[1] -= 18
                    new_bullet = Bullet(pos, 6, 30, -1)
                    new_bullet.setImage("img/bullet.png", 36/2, 56/2)
                    entityManager.addEntity(new_bullet)
                    waveGenerator.playerBullets.append(new_bullet)
    
    # for event in sense.stick.get_events():
    #     if(event.action == "pressed"):
    #         print("PIOU!!")
    
    # player._speed = calculateVelocity(accelerometer)

    pygame.display.flip()
    clock.tick(60)
