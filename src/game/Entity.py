import pygame
from pygame import sprite
from pygame import image

SHOOT_TOP = 1
SHOOT_RIGHT = 2
SHOOT_BOTTOM = -1
SHOOT_LEFT = 2

class Entity(sprite.Sprite):
    _position = [0, 0] 
    _speed = 0
    _damage = 0
    _shoot_direction = SHOOT_BOTTOM

    image = None
    rect = None
    
    def __init__(self):
        super().__init__()
    
    def initProperties(self):
        pass

    def setPosition(self, new_position: list[int,int]) -> None:
        self._position = new_position

    def toString(self) -> str:
        return 'position ' + str(self._position) + ' speed: ' + str(self._speed) + ' damage: '+ str(self._damage) + ' shot_direction: ' + str(self._shoot_direction)

    def shot(self):
        pass


    def setImage(self, url, width, height):
        self.image = pygame.transform.scale(image.load(url).convert_alpha(), (width, height))
        self.rect = self.image.get_rect()
    
    def draw(self, screen):
        pass
