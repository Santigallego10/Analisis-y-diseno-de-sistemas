from model.ProductsFactoryPattern.Product import Product


class DecorativeProductColor(Product):

    def __init__(self, color):
        self.color = color
