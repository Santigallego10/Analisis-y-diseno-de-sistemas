from abc import ABC, abstractmethod


class ProductService(ABC):

    @abstractmethod
    def addProduct(self):
        pass

    @abstractmethod
    def updateProduct(self):
        pass

    @abstractmethod
    def deleteProduct(self):
        pass

    @abstractmethod
    def getProducto(self):
        pass
