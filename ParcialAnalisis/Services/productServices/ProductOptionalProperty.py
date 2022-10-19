from abc import ABC, abstractmethod

'''
This class represents the interfaz of product category
'''


class ProductOptionalProperty(ABC):

    @abstractmethod
    def getProperty(self):
        pass
