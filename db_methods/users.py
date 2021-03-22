from db_contexts.rpsbot_context import rps_db
from models.user import User
from .repository import Repository


class UsersJobs(Repository):
    def __init__(self):
        super().__init__(rps_db)

    def insert_user(self, user: User):
        self.session.add(user)
        self.commit()

    def get_user(self, telegram_id: int) -> User:
        return self.session.query(User).filter_by(
            telegram_id=telegram_id).first()

    def delete_user(self, telegram_id: int):
        user = self.get_user(telegram_id)
        self.session.delete(user)
        self.commit()

    def get_all_count(self) -> int:
        return self.session.query(User).count()

    def exists(self, telegram_id: int) -> bool:
        return self.session.query(User).filter_by(
            telegram_id=telegram_id).count() == 1
