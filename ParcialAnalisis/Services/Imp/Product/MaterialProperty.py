from Services.productServices.ProductOptionalProperty import ProductOptionalProperty

class MaterialProperty(ProductOptionalProperty):

    def __init__(self, materialName):
        self.name = materialName

    def getProperty(self):
        return self.name