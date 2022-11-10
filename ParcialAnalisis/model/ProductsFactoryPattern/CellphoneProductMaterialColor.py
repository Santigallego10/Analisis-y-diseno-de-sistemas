from model.ProductsFactoryPattern.Product import Product


class CellphoneProductMaterialColor(Product):

    def __init__(self, material, color):
        self.material = material
        self.color = color
