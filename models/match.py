from sqlalchemy import Column, Integer, String, DateTime, Boolean, JSON
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class GroupMatch(Base):
    __tablename__ = 'group_match'
    id = Column(Integer, primary_key=True)
    match_id = Column(String, nullable=False)
    group_id = Column(Integer, nullable=False)
    creator = Column(Integer, nullable=False)
    create_date = Column(DateTime, nullable=False)
    finished = Column(Boolean, nullable=False)
    started = Column(Boolean)
    players_status = Column(JSON)
