from db_contexts.rpsbot_context import rps_db
from models.user import User
from .repository import Repository


class UsersJobs(Repository):
    def __init__(self):
        super().__init__(rps_db, User)

    def insert_user(
        self,
        telegram_id: int,
        name: str,
        username=None,
        lang_code=None
    ):
        self.session.add(User(telegram_id, name, username, lang_code))
        self.commit()

    def update(self, user: User, name=None, username=None, lang_code=None):
        if name:
            user.name = name
        if username:
            user.username = username
        if lang_code:
            user.lang_code = lang_code
        self.commit()

    def get_user(self, telegram_id: int) -> User:
        return self.query.filter_by(
            telegram_id=telegram_id).first()

    def delete_user(self, telegram_id: int):
        user = self.get_user(telegram_id)
        self.session.delete(user)
        self.commit()

    def get_all_count(self) -> int:
        return self.query.count()

    def exists(self, telegram_id: int) -> bool:
        return self.query.filter_by(
            telegram_id=telegram_id).count() == 1
