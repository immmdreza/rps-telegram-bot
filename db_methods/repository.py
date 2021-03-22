from db_contexts.context_base import DbContext
from abc import ABC


class Repository(ABC):
    def __init__(self, context: DbContext):
        self.__context = context

    def commit(self):
        return self.session.commit()

    def __enter__(self):
        self.session = self.__context.Session()
        return self

    def __exit__(self, type, value, traceback):
        self.session.close()
        return False
