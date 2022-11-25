from game.Entity import Entity

class Bullet(Entity):
    def __init__(self, position):
        self.super()
        self.initPosition(position)

    def initPosition(self, position):
        self._position = position