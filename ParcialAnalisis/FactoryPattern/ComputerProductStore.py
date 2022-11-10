from FactoryPattern.ProductStore import ProductStore
from model.ProductsFactoryPattern import ComputerProduct
from model.ProductsFactoryPattern import ComputerProductMaterialColor
from model.ProductsFactoryPattern import ComputerProductMaterial
from model.ProductsFactoryPattern import ComputerProductColor

'''
    THIS CLASS MANAGE THE CREATION OF ANY OF THE PRODUCT VARIATIONS
    PRESENT IN THIS CATEGORY

'''


class ComputerProductStore(ProductStore):

    def __init__(self):
        pass

    def createProduct(self, typeName):
        if typeName == "Product":
            return ComputerProduct()
        elif typeName == "ProductColor":
            return ComputerProductColor(input("Write the color of the product"))
        elif typeName == "ProductMaterial":
            return ComputerProductMaterial(input("Write the material of the product"))
        elif typeName == "ProductMaterialColor":
            return ComputerProductMaterialColor(input("Write the material of the product"),input("Write the color of the product"))
        return None
