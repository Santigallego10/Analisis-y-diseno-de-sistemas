from model.ProductsFactoryPattern.Product import Product


class AccessoryProductMaterial(Product):

    def __init__(self, material):
        self.material = material
