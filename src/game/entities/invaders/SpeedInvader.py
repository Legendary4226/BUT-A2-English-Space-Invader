from Invader import Invader

class SpeedInvader (Invader):
    def __init__(self):
        initProperties()

    #Override
    def setProperties(self) -> None:
        self.damage = 5
        self.max_hp  = 70
        self.hp = 70
        self.shot_speed = 30