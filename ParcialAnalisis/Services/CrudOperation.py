from abc import ABC, abstractmethod


class CrudOperation(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def detele(self):
        pass

    @abstractmethod
    def get(self):
        pass
