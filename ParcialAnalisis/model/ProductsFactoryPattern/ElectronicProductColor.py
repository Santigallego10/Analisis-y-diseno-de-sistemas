from model.ProductsFactoryPattern.Product import Product


class ElectronicProductColor(Product):

    def __init__(self, color):
        self.color = color
