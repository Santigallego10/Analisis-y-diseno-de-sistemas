from Services.productServices.ProductOptionalProperty import ProductOptionalProperty

'''
This class represents an optional property for a product
'''


class MaterialProperty(ProductOptionalProperty):

    def __init__(self, materialName):
        self.name = materialName

    def getProperty(self):
        return self.name