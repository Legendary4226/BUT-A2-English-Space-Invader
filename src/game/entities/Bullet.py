from game.Entity import Entity

class Bullet(Entity):
    def __init__(self, position: list[int,int], speed: int, damage: int, shoot_direction: int) -> None:
        self.initProperties(position,speed,damage,shoot_direction)

    def initProperties(self, position: list[int,int], speed: int, damage: int, shoot_direction: int) -> None:
        self._position = position 
        self._speed = speed
        self._damage = damage
        self._shoot_direction = shoot_direction