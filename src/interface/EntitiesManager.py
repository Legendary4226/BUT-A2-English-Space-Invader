class EntityManager:
    entities = []


    def __init__(self) -> None:
        pass

    def clear(self):
        for entity in self.entities:
            del entity

    def draw(self):
        for entity in self.entities:
            entity.draw()

    def event(self, events):
        # TO DO
        pass
