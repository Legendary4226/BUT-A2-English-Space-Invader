from game.Entity import Entity, SHOOT_TOP
from game.entities.Bullet import Bullet

class Ship(Entity):
    _hp = 0
    _shoot_speed = 0
    _shoot_direction = SHOOT_TOP        
    
    def takeDamage(self, damage: int) -> None:
        self._hp -= damage
        if (self._hp < 0):
            self._hp = 0

    def isDead(self) -> bool:
        return self._hp == 0

    def isAlive(self) -> bool:
        return self._hp > 0
    
    def shot(self) -> None:
        bul = Bullet(self._position, self._shoot_speed, self._damage, self._shoot_direction)
        return bul.toString()

    def toString(self) -> str:
        return super().toString()+ ' hp: '+ str(self._hp)+ ' shot_speed: '+ str(self._shoot_speed)+ ' shot_direction: '+ str(self._shoot_direction)
    