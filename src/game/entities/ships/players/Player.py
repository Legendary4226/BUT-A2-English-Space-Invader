from game.entities.Ship import Ship
from game.Entity import SHOOT_TOP

class Player (Ship):
    def __init__(self):
        self.initProperties()

    def initProperties(self) -> None:
        self._damage = 10
        self._max_hp  = 100
        self._hp = 100
        self._speed = 20
        self._shoot_speed = 20
        self._shoot_direction = SHOOT_TOP
    
    def cure(self) -> None:
        self._hp += 10
        if (self._hp > self._max_hp):
            self._hp = self._max_hp

    def boostDamage(self) -> None:
        self._damage += 5

    def boostSpeed(self) -> None:
        self._shoot_speed += 5
        self._speed += 5