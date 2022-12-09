from game.entities.Ship import Ship
from game.Entity import SHOOT_BOTTOM

class Invader (Ship):
    _shoot_direction = SHOOT_BOTTOM
    
    def __init__(self) -> None:
        self.initProperties()

    def initProperties(self) -> None:
        self._damage = 10
        self._max_hp  = 100
        self._hp = 100
        self._speed = 20
        self._shoot_speed = 20
