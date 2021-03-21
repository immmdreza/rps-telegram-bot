from .context_base import DbContext

class RpsDb(DbContext):
    def __init__(self):
        super().__init__('sqlite:///rpsbot-database.db')

rps_db = RpsDb()
