from model.ProductsFactoryPattern.Product import Product


class ElectronicProductMaterialColor(Product):

    def __init__(self,material,color):
        self.material = material
        self.color = color


