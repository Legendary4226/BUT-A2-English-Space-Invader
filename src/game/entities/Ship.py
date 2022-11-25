from game.Entity import Entity, SHOOT_TOP
from game.entities.Bullet import Bullet

class Ship(Entity):
    def __init__(self):
        super()
        
        self._shoot_speed = 0
        self._shoot_direction = SHOOT_TOP
    
    def initProperties(self) -> None:
        self._damage = 10
        self._max_hp  = 100
        self._hp = 100
        self._shoot_speed = 20
    
    def shot(self):
            Bullet(self._position, self._shoot_direction)
        
    