SHOOT_TOP = 1
SHOOT_RIGHT = 2
SHOOT_BOTTOM = -1
SHOOT_LEFT = 2

class Entity:
    _position = [0, 0] 
    _speed = 0
    _damage = 0
    _shoot_direction = SHOOT_BOTTOM
    
    def initProperties(self) -> None:
        pass

    def setPosition(self, new_position: list[int,int]) -> None:
        self._position = new_position

    def toString(self) -> str:
        return 'position ' + str(self._position) + ' speed: ' + str(self._speed) + ' damage: '+ str(self._damage) + ' shot_direction: ' + str(self._shoot_direction)
