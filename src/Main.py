import random
from game.Entity import Entity
from game.entities.Ship import Ship
from game.entities.Collectable import Collectable
from game.entities.Bullet import Bullet
from game.entities.ships.Invader import Invader
from game.entities.ships.invadersType.EavyInvader import EavyInvader
from game.entities.ships.invadersType.NormalInvader import NormalInvader
from game.entities.ships.invadersType.SpeedInvader import SpeedInvader
from game.entities.ships.players.Player import Player


if __name__ == '__main__':
    entity = Entity()
    if True:
        ship = Ship()
        if True:
            player = Player()
            invader = Invader()
            if True:
                eavy = EavyInvader()
                normal = NormalInvader()
                speed = SpeedInvader()
    if True:
        collectable = Collectable(None,None,None)
        bullet = Bullet(None,None,None,None)
            
    """
    print('entity: ' , entity.toString())
    print()
    print('invader: ', invader.toString())
    print()
    print('eavy: ', eavy.toString())
    print()
    print('normal: ', normal.toString())
    print()
    print('speed: ', speed.toString())"""
    print(eavy.shot())
    print(player.shot())
    