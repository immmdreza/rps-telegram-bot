from sqlalchemy.orm import reconstructor


class EntityBase:

    @reconstructor
    def init_on_load(self):
        self.__repository = None
