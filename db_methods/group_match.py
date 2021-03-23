from db_contexts.rpsbot_context import rps_db
from models.match import GroupMatch
from .repository import Repository
from datetime import datetime


class GroupMatchJobs(Repository):
    def __init__(self):
        super().__init__(rps_db, GroupMatch)

    def get_match(self, match_id: str):
        return self.query.filter_by(
            match_id=match_id).first()

    def has_unfinished_match(self, group_id: int):
        return self.query.filter_by(
            group_id=group_id, finished=False).count() >= 1

    def unfinished_match(self, group_id: int) -> GroupMatch:
        return self.query.filter_by(
            group_id=group_id, finished=False).first()

    def add_match(self, match_id: str, group_id: int, creator: int):
        self.session.add(
            GroupMatch(
                match_id=match_id,
                group_id=group_id,
                creator=creator,
                create_date=datetime.utcnow(),
                finished=False,
                started=False
            )
        )
        self.commit()

    def remove_match_by_id(self, match_id: str):
        match = self.get_match(match_id)
        self.session.delete(match)
        self.commit()

    def remove_match(self, match: GroupMatch):
        self.session.delete(match)
        self.commit()
