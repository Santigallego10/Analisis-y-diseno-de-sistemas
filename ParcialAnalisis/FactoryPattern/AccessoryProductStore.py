from FactoryPattern.ProductStore import ProductStore
from model.ProductsFactoryPattern.AccessoryProduct import AccessoryProduct
from model.ProductsFactoryPattern.AccessoryProductMaterialColor import AccessoryProductMaterialColor
from model.ProductsFactoryPattern.AccessoryProductMaterial import AccessoryProductMaterial
from model.ProductsFactoryPattern.AccessoryProductColor import AccessoryProductColor


class AccessoryProductStore(ProductStore):

    def __init__(self):
        pass

    def createProduct(self, typeName):
        product = None
        if typeName == "Product":
            return AccessoryProduct()
        elif typeName == "ProductColor":
            return AccessoryProductColor(input("Write the color of the product"))
        elif typeName == "ProductMaterial":
            return AccessoryProductMaterial(input("Write the material of the product"))
        elif typeName == "ProductMaterialColor":
            return AccessoryProductMaterialColor(input("Write the material of the product"),input("Write the color of the product"))
        return None
