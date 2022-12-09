import random
from game.Entity import Entity, SHOOT_BOTTOM


class Collectable(Entity):
    _benefit_effect = None

    def __init__(self, position: list[int,int], speed: int, damage: int):
        self.initProperties(position, speed, damage)

    def initProperties(self, position: list[int,int], speed: int, damage: int) -> None:
        self._position = position 
        self._speed = speed
        self._damage = damage
        self._shoot_direction = SHOOT_BOTTOM
        self._benefit_effect = random.randint(1,3);
