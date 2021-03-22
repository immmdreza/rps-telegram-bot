from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class DbContext:
    def __init__(self, addr: str):
        self.__engine = create_engine(addr, echo=False)

    def new_session(self, f):
        def wapper(*args, **kwargs):
            with self.Session() as session:
                with session.begin():
                    return f(session, *args, **kwargs)
        return wapper

    def new_no_expire_session(self, f):
        def wapper(*args, **kwargs):
            with self.Session() as session:
                with session.begin():
                    return f(session, *args, **kwargs)
        return wapper

    def Session(self, expire_on_commit=True) -> Session:
        return Session(self.__engine, expire_on_commit=expire_on_commit)
