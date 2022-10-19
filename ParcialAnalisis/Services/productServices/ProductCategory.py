from abc import ABC, abstractmethod


class ProductCategory(ABC):

    @abstractmethod
    def getCategory(self):
        pass
