from db_contexts.rpsbot_context import rps_db
from models.user import User

# ed_user = User(name='Ed Jones', username='edsnickname', lang_code = "fa")
# rps_db.Session.add(ed_user)

# rps_db.commit()

our_user = rps_db.Session.query(User).filter_by(name='Ed Jones').first()

print(our_user.username)
