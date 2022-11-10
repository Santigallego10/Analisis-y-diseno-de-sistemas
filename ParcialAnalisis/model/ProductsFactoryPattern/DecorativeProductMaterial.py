from model.ProductsFactoryPattern.Product import Product


class DecorativeProductMaterial(Product):

    def __init__(self, material):
        self.material = material

