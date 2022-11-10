from model.ProductsFactoryPattern.Product import Product


class CellphoneProductMaterial(Product):

    def __init__(self, material):
        self.material = material