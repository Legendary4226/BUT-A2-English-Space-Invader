from game.entities.ships.Invader import Invader

class NormalInvader (Invader):
    def __init__(self):
        self.initProperties()

    def initProperties(self) -> None:
        self._damage = 15
        self._max_hp  = 100
        self._hp = 80
        self._speed = 1.2
        self._shoot_speed = 20
