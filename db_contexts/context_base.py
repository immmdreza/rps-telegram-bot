from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbContext:
    def __init__(self, addr: str):
        self.__engine = create_engine(addr, echo=False)
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
