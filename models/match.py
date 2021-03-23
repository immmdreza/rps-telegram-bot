from sqlalchemy import Column, Integer, String, DateTime, Boolean, JSON
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class GroupMatch(Base):
    __tablename__ = 'group_match'
    id = Column(Integer, primary_key=True)
    match_id = Column(String)
    group_id = Column(Integer)
    creator = Column(Integer)
    create_date = Column(DateTime)
    finished = Column(Boolean)
    started = Column(Boolean)
    players_status = Column(JSON)
