from sqlalchemy import Column, Integer, String
from .base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    lang_code = Column(String)

    def __repr__(self):
       return "<User(name='%s', username='%s', lang code='%s')>" % (
                            self.name, self.username, self.lang_code)