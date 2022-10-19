class Product:

    def __init__(self, name, sku, description,
                 price, material, color, category,stock
                 , images, creationDate, updatingDate):
        self.name = name
        self.sku = sku
        self.description = description
        self.price = price
        self.material = material
        self.color = color
        self.category = category
        self.stock = stock
        self.images = []
        self.creationDate = creationDate
        self.updatingDate = updatingDate
