from app.repositories import AbstractRepository


class UserUseCases:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def get_user(self, id: int):
        return self.repository.get(id)
