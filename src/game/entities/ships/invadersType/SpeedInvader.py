from game.entities.ships.Invader import Invader

class SpeedInvader (Invader):
    def __init__(self: Invader):
        self.initProperties()

    def initProperties(self) -> None:
        self._damage = 5
        self._max_hp  = 75
        self._hp = 75
        self._speed = 30
        self._shoot_speed = 30

