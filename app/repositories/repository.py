import abc

from app.models import User


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, id: int) -> User:
        pass

    @abc.abstractmethod
    def update(self, reference) -> User:
        pass

    @abc.abstractmethod
    def delete(self, reference) -> User:
        pass

    @abc.abstractmethod
    def insert(self, reference) -> User:
        pass
