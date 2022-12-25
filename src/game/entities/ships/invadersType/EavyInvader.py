from game.entities.ships.Invader import Invader

class EavyInvader (Invader):
    def __init__(self):
        self.initProperties()

    def initProperties(self) -> None:
        self._damage = 30
        self._max_hp  = 250
        self._hp = 150
        self._speed = 0.5
        self._shoot_speed = 20
    
