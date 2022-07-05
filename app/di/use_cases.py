from app.di.repositories import get_postgresql_repository
from app.use_cases import UserUseCases


def get_user_use_case() -> UserUseCases:
    repository = get_postgresql_repository()
    return UserUseCases(repository=repository)
