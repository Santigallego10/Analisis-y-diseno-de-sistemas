from abc import ABC, abstractmethod


class ProductOptionalProperty(ABC):

    @abstractmethod
    def getProperty(self):
        pass
