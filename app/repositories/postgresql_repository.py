from sqlalchemy import Table, Column, Integer, String

from app.db import PostgreSQLConnector
from app.models import User
from app.repositories.repository import AbstractRepository


class PostgreSQLRepository(AbstractRepository):
    def __init__(self):
        self.db = PostgreSQLConnector()
        self.user = Table("user", self.db.meta,
                          Column("id", Integer, primary_key=True),
                          Column("username", String(128)),
                          Column("password", String(128)),
                          extend_existing=True
                          )
        self.db.meta.create_all(self.db.engine)

    def get(self, id: int) -> User:
        result = self.db.conn.execute(self.user.select().where(self.user.c.id == id)).first()
        return User(**result) if result else None

    def update(self, reference) -> User:
        pass

    def delete(self, reference) -> User:
        pass

    def insert(self, reference) -> User:
        pass
