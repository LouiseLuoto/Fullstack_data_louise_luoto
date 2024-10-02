from backend.database import DatabaseDataframe
from backend.constants import DATABASE_PATH


class QueryDatabase:
    def __init__(self, sql_query) -> None:
        with DatabaseDataframe(DATABASE_PATH) as db:
            self.df = db.query(sql_query)