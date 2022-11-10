from abc import ABC, abstractmethod

'''
THIS CLASS IS USED TO FOLLOW THE FACTORY METHOD PATTERN

THIS ABSTRACT CLASS REPRESENTS THE MAIN STORE, IS USED TO
DEFINE THE METHODS THAT THE CONCRETE STORES WILL IMPLEMENT
'''

class ProductStore(ABC):

    @abstractmethod
    def createProduct(self, typeName):
        pass




