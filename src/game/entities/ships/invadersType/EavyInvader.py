from game.entities.ships.Invader import Invader

class EavyInvader (Invader):
    def __init__(self):
        self.initProperties()

    def initProperties(self) -> None:
        self._damage = 20
        self._max_hp  = 250
        self._hp = 250
        self._speed = 0.05
        self._shoot_speed = 20
    
