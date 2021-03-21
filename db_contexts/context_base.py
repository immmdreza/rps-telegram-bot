from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

class DbContext:
    def __init__(self, addr: str):
        self.__engine = create_engine(addr, echo=False)
        Session = sessionmaker(bind=self.__engine)
        self.__session: Session = Session()

    def commit(self):
        return self.__session.commit()

    @property
    def Session(self) -> Session:
        return self.__session