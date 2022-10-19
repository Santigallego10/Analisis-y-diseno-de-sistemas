from abc import ABC, abstractmethod

'''
This class represents the interfaz of product category
'''


class ProductCategory(ABC):

    @abstractmethod
    def getCategory(self):
        pass
