from Services.productServices.ProductCategory import ProductCategory

class Product:

    '''
    This class owns a list of optional properties that can be
      set as instance of the class: ProductOptionalProperty

    This class owns a category that must be and instance of
      the class: ProductCategory
    '''

    productOptionalProperties = []
    category: ProductCategory

    def __init__(self, name, sku, description,
                 price, properties, category,stock
                 , images, creationDate, updatingDate):
        self.name = name
        self.sku = sku
        self.description = description
        self.price = price
        self.optionalProperties = properties
        self.category = category
        self.stock = stock
        self.images = []
        self.creationDate = creationDate
        self.updatingDate = updatingDate
