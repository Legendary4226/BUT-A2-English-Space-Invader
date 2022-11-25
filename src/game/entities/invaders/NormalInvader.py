from Invader import Invader

class NormalInvader (Invader):
    def __init__(self):
        initProperties()

    #Override
    def setProperties(self) -> None:
        self.damage = 10
        self.max_hp  = 100
        self.hp = 100
        self.shot_speed = 20