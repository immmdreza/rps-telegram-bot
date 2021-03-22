from db_methods.users import UsersJobs
from models.user import User


with UsersJobs() as uj:
    if not uj.exists(123456):
        uj.insert_user(User(123456, "AraSH"))

        user = uj.get_user(123456)
        print(user.name)
    else:
        uj.delete_user(123456)
