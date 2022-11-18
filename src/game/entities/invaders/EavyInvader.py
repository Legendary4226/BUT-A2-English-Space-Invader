from Invader import Invader

class EavyInvader (Invader):
    def __init__(self):
        initProperties()

    #Override
    def setProperties(self) -> None:
        self.damage = 20
        self.max_hp  = 250
        self.hp = 250
        self.shot_speed = 10