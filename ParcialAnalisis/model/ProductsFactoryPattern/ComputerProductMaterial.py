from model.ProductsFactoryPattern.Product import Product


class ComputerProductMaterial(Product):

    def __init__(self, material):
        self.material = material
