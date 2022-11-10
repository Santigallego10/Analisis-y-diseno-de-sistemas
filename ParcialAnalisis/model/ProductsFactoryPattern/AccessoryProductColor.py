from model.ProductsFactoryPattern.Product import Product


class AccessoryProductColor(Product):

    def __init__(self, color):
        self.color = color
