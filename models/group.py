from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class GroupInfo(Base):
    __tablename__ = 'group_info'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    creator = Column(Integer, nullable=False)
    admins = Column(JSON)
    first_join_date = Column(DateTime)
    last_join_date = Column(DateTime)
    games_count = Column(Integer, nullable=False)
    last_game_date = Column(DateTime)
    maximum_players = Column(Integer, nullable=False)

    def __init__(
        self,
        group_id: int,
        title: str,
        creator: int,
        admins: str = '[]'
    ) -> None:
        self.group_id = group_id
        self.title = title,
        self.creator = creator
        self.admins = admins
        self.games_count = 0,
        self.maximum_players = 0
