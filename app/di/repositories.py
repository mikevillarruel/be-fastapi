from app.repositories import PostgreSQLRepository


def get_postgresql_repository() -> PostgreSQLRepository:
    return PostgreSQLRepository()
