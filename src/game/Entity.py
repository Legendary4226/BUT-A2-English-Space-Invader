from pygame import sprite
from pygame import image

SHOOT_TOP = 1
SHOOT_RIGHT = 2
SHOOT_BOTTOM = -1
SHOOT_LEFT = 2

class Entity(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._position = [0, 0]

        self._hp = 0 # not
        self._speed = 0
        self._damage = 0
        self._shoot_direction = SHOOT_BOTTOM

        self.image = None
        self.rect = None
    
    def initProperties(self):
        pass

    def setPosition(self, new_position) -> None:
        self._position = new_position

    def setSpeed(self, new_speed):
        self._speed = new_speed

    def takeDamage(self, damage) -> None:
        self._hp -= damage
        if (self._hp < 0):
            self._hp = 0

    def isDead(self) -> bool:
        return self._hp == 0

    def isAlive(self) -> bool:
        return self._hp > 0

    def shot(self):
        pass


    def setImage(url):
        self.image = image.load(url)
        self.rect = self.image.get_rect()
