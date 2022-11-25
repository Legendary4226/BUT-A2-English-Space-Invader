from Entity import Entity

class Invader (Entity):
    def __init__(self):
        super(self)
    
    def setProperties(self) -> None:
        pass

    def setPosition(self, new_position) -> None:
        self.position = new_position

    def takeDamage(self, damage) -> None:
        if (self.hp - damage == 0):
            self.hp = 0
        else:
            self.hp -= damage