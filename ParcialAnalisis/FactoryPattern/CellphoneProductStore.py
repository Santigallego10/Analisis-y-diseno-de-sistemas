from FactoryPattern.ProductStore import ProductStore
from model.ProductsFactoryPattern import CellphoneProduct
from model.ProductsFactoryPattern import CellphoneProductMaterialColor
from model.ProductsFactoryPattern import CellphoneProductMaterial
from model.ProductsFactoryPattern import CellphoneProductColor


class CellphoneProductStore(ProductStore):

    def __init__(self):
        pass

    @staticmethod
    def createProduct(typeName):
        if typeName == "Product":
            return CellphoneProduct()
        elif typeName == "ProductColor":
            return CellphoneProductColor(input("Write the color of the product"))
        elif typeName == "ProductMaterial":
            return CellphoneProductMaterial(input("Write the material of the product"))
        elif typeName == "ProductMaterialColor":
            return CellphoneProductMaterialColor(input("write the material of the product"),input("Write the color of the product"))
        return None
