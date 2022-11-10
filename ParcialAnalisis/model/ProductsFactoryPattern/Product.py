class Product:

    '''
    This class owns a list of optional properties that can be
      set as instance of the class: ProductOptionalProperty

    This class owns a category that must be and instance of
      the class: ProductCategory

      All the possible variation of a product extend from this specific class
    '''

    def __init__(self, name, sku, description,
                 price, stock, images, creationDate, updatingDate):
        self.name = name
        self.sku = sku
        self.description = description
        self.price = price
        self.stock = stock
        self.images = images
        self.creationDate = creationDate
        self.updatingDate = updatingDate




