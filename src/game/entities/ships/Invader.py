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
        self._speed = 0
        self._shoot_speed = 20

    def draw(self, screen):
        screen.blit(self.image, self._position)

        # Move
        self._position[1] += self._speed

