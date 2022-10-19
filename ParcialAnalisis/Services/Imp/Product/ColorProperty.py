from Services.productServices.ProductOptionalProperty import ProductOptionalProperty

class ColorProperty(ProductOptionalProperty):

    def __init__(self, color):
        self.color = color

    def getProperty(self):
        return self.color