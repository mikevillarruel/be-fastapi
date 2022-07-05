from sqlalchemy import MetaData, create_engine


class BaseConnector:

    DB_URL: str = None

    def __init__(self):
        self.engine = create_engine(self.DB_URL)
        self.meta = MetaData()
        self.conn = self.engine.connect()
