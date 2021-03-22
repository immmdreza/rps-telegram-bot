from .base import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    name = Column(String)
    username = Column(String)
    lang_code = Column(String)

    def __init__(
        self, telegram_id: int, name: str, username=None, lang_code='en'
    ):
        self.name = name
        self.telegram_id = telegram_id
        self.username = username
        self.lang_code = lang_code

    def __repr__(self):
        return "<User(name='{}' ({}), username='{}', lang code='{}')>".format(
            self.name,
            self.telegram_id,
            self.username,
            self.lang_code)
