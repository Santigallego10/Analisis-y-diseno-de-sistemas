from FactoryPattern.ProductStore import ProductStore
from model.ProductsFactoryPattern import DecorativeProduct
from model.ProductsFactoryPattern import DecorativeProductMaterialColor
from model.ProductsFactoryPattern import DecorativeProductMaterial
from model.ProductsFactoryPattern import DecorativeProductColor

'''
    THIS CLASS MANAGE THE CREATION OF ANY OF THE PRODUCT VARIATIONS
    PRESENT IN THIS CATEGORY

'''


class DecorativeProductStore(ProductStore):

    def __init__(self):
        pass

    @staticmethod
    def createProduct(typeName):
        if typeName == "Product":
            return DecorativeProduct()
        elif typeName == "ProductColor":
            return DecorativeProductColor(input("Write the color of the product"))
        elif typeName == "ProductMaterial":
            return DecorativeProductMaterial(input("Write the material of the product"))
        elif typeName == "ProductMaterialColor":
            return DecorativeProductMaterialColor(input("Write the material of the product"),input("Write the color of the product"))
        return None
