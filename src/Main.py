import pygame
from pygame.locals import *
from interface.EntitiesManager import EntityManager

from game.entities.ships.players.Player import Player
from game.entities.Bullet import Bullet
from game.WaveGenerator import WaveGenerator



### Init Global Variables

pygame.init()

font = pygame.font.SysFont("Arial", 20, bold=False, italic=False)

width = 1280
height = 720
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('SPACE INVADER')


### Init Game Variables

entityManager = EntityManager()

player = Player()
player.setImage("src/img/ship.png", 50, 50)
entityManager.addEntity(player)
player._position = [width/2, 9*height/10]

playerBullets = []

waveGenerator = WaveGenerator(player, entityManager, screen)

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
                    player._speed = -.5
                if event.key == pygame.K_d:
                    player._speed = .5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q or event.key == pygame.K_d:
                    player._speed = 0
                if event.key == pygame.K_SPACE:
                    pos = player._position.copy()
                    pos[0] += 16
                    pos[1] -= 18
                    new_bullet = Bullet(pos, 0.15, 10, -1)
                    new_bullet.setImage("src/img/bullet.png", 36/2, 56/2)
                    entityManager.addEntity(new_bullet)
                    waveGenerator.playerBullets.append(new_bullet)
                    

    pygame.display.flip()
