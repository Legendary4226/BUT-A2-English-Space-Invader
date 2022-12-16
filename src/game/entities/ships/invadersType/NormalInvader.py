from game.entities.ships.Invader import Invader

class NormalInvader (Invader):
    def __init__(self):
        self.initProperties()

    def initProperties(self) -> None:
        self._damage = 10
        self._max_hp  = 100
        self._hp = 100
        self._speed = 0.1
        self._shoot_speed = 20
