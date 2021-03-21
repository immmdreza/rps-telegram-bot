from db_contexts.rpsbot_context import RpsDb
from models.user import User

db = RpsDb()

ed_user = User(name='Ed Jones', username='edsnickname', lang_code = "fa")
db.session.add(ed_user)

db.session.commit()