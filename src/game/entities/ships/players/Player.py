from game.entities.Ship import Ship
from game.Entity import SHOOT_TOP

class Player (Ship):
    def __init__(self):
        self.initProperties()

    def initProperties(self) -> None:
        self._damage = 10
        self._max_hp  = 100
        self._hp = 100
        self._speed = 0
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
    
    def draw(self, screen):
        screen.blit(self.image, self._position)

        # Move
        self._position[0] += self._speed

        if (self._position[0] < 0):
            self._position[0] = 0
        if (self._position[0] > screen.get_width() - 50):
            self._position[0] = screen.get_width() - 50
