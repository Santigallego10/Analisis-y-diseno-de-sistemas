from abc import ABC, abstractmethod


class ProductStore(ABC):

    @abstractmethod
    def createProduct(self, typeName):
        pass




