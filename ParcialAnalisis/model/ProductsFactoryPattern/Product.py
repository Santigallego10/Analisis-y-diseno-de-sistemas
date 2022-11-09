class Product:

    '''
    This class owns a list of optional properties that can be
      set as instance of the class: ProductOptionalProperty

    This class owns a category that must be and instance of
      the class: ProductCategory
    '''

    def __init__(self, name, sku, description,
                 price,stock, images, creationDate, updatingDate):
        self.name = name
        self.sku = sku
        self.description = description
        self.price = price
        self.stock = stock
        self.images = []
        self.creationDate = creationDate
        self.updatingDate = updatingDate
