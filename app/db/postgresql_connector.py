from app.db import BaseConnector
from app.utils import EnvConfig


class PostgreSQLConnector(BaseConnector):
    DB_URL = EnvConfig.DB_URL
