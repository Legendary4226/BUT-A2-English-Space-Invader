from game.entities.Bullet import Bullet
from game.entities.Ship import Ship
from game.entities.ships.invadersType.EavyInvader import EavyInvader
from game.entities.ships.invadersType.NormalInvader import NormalInvader
from game.entities.ships.invadersType.SpeedInvader import SpeedInvader
from interface.EntitiesManager import EntityManager
from random import random, randint



class WaveGenerator:
    def __init__(self, ship : Ship, entityManager : EntityManager, screen) -> None:
        self.playerBullets = []
        self.enemiesBullets = []
        self.enemies = []
        self.ship = ship
        self.entityManager = entityManager
        self.screen = screen

    def update(self):
        # Generate a wave
        generate = random() < 0.011

        if generate:
            type = random()

            newInvader = None
            if type < 0.20: # 20%
                newInvader = SpeedInvader()
                newInvader.setImage("img/invader3.png", 30, 30)
            elif type < 0.9: # 70%
                newInvader = NormalInvader()
                newInvader.setImage("img/invader2.png", 40, 40)
            else:              # 10%
                newInvader = EavyInvader()
                newInvader.setImage("img/invader1.png", 50, 50)
            
            if (newInvader is not None):
                newInvader._position = [randint(0, self.screen.get_width() - 50), 0]
                self.addEnemy(newInvader)


        for playerBullet in self.playerBullets:
            for enemy in self.enemies:
                ePosX = enemy._position[0] - playerBullet.size[0]/2
                ePosY = enemy._position[1] - playerBullet.size[1]/2
                ePosXmax = enemy._position[0] + enemy.size[0] + playerBullet.size[0]/2
                ePosYmax = enemy._position[1] + enemy.size[1] + playerBullet.size[1]/2

                bPosX = playerBullet._position[0] + playerBullet.size[0]/2
                bPosY = playerBullet._position[1]

                if (ePosX <= bPosX and bPosX <= ePosXmax) and (ePosY <= bPosY and bPosY <= ePosYmax):
                    enemy._hp -= playerBullet._damage
                    self.deletePlayerBullet(playerBullet)


        # Clear entities
        for playerBullet in self.playerBullets:
            if (playerBullet._position[1] < 0):
                self.deletePlayerBullet(playerBullet)
        
        # for enemyBullet in self.enemiesBullets:
        #     if (enemyBullet._position[1] > self.screen.get_height()):
        #         self.deleteEnemyBullet(enemyBullet)
        
        for enemy in self.enemies:
            if enemy._position[1] > self.screen.get_height():
                self.ship._hp -= enemy._damage
                self.deleteEnemy(enemy)
            if enemy._hp <= 0:
                self.deleteEnemy(enemy)
                
        
        if self.ship._hp <= 0:
            exit()




    def addEnemy(self, enemy):
        self.entityManager.addEntity(enemy)
        self.enemies.append(enemy)
        del enemy

    def deletePlayerBullet(self, bullet):
        self.entityManager.deleteEntity(bullet)
        self.playerBullets.remove(bullet)
        del bullet

    def deleteEnemyBullet(self, bullet):
        self.entityManager.deleteEntity(bullet)
        self.enemiesBullets.remove(bullet)
        del bullet
        print("ENEMY BULLET DELETED")

    def deleteEnemy(self, enemy):
        self.entityManager.deleteEntity(enemy)
        self.enemies.remove(enemy)
        del enemy