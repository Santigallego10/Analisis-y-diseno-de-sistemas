from Services.productServices.ProductCategory import ProductCategory

class Product:

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
