from FactoryPattern.ProductStore import ProductStore
from model.ProductsFactoryPattern import ElectronicProduct
from model.ProductsFactoryPattern import ElectronicProductMaterialColor
from model.ProductsFactoryPattern import ElectronicProductMaterial
from model.ProductsFactoryPattern import ElectronicProductColor


class ElectronicProductStore(ProductStore):

    def __init__(self):
        pass

    @staticmethod
    def createProduct(typeName):
        if typeName == "Product":
            return ElectronicProduct()
        elif typeName == "ProductColor":
            return ElectronicProductColor(input("Write the color of the product"))
        elif typeName == "ProductMaterial":
            return ElectronicProductMaterial(input("Write the material of the product"))
        elif typeName == "ProductMaterialColor":
            return ElectronicProductMaterialColor(input("Write the material of the product"),input("Write the color of the product"))
        return None

