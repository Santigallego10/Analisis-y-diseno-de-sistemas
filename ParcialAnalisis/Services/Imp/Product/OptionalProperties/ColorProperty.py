from Services.productServices.ProductOptionalProperty import ProductOptionalProperty

'''
This class represents an optional property for a product
'''


class ColorProperty(ProductOptionalProperty):

    def __init__(self, color):
        self.color = color

    def getProperty(self):
        return self.color