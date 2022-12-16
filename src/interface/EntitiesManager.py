class EntityManager:
    entities = []


    def __init__(self) -> None:
        pass
    

    def addEntity(self, entity):
        self.entities.append(entity)

    def deleteEntity(self, entity):
        self.entities.remove(entity)

    def clear(self):
        for entity in self.entities:
            self.entities.remove(entity)
            del entity

    def draw(self, screen):
        for entity in self.entities:
            entity.draw(screen)
