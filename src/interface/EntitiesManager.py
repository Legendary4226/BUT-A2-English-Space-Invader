class EntityManager:
    entities = []


    def __init__(self) -> None:
        pass
    

    def addEntity(self, entity):
        self.entities.append(entity)

    def clear(self):
        for entity in self.entities:
            self.entities.remove(entity)
            del entity

    def draw(self):
        for entity in self.entities:
            entity.draw()

    def event(self, events):
        # TO DO
        pass
