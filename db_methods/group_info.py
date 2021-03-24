from typing import List
from db_contexts.rpsbot_context import rps_db
from models.group import GroupInfo
from db_methods.repository import Repository
import json


class GroupInfoJobs(Repository):
    def __init__(self):
        super().__init__(rps_db, GroupInfo)

    def insert_info(
        self,
        group_id,
        title,
        creator_id,
        admins: List[int]
    ):
        self.session.add(
            GroupInfo(
                group_id,
                title,
                creator_id,
                json.dumps(admins)
            )
        )
        self.commit()
