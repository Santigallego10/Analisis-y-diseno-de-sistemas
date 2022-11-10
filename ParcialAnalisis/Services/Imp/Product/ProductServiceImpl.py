from Services.productServices.ProductService import ProductService

'''
This class implements the interface ProductService 
This class owns the list of products
'''


def getProductType():
    isMaterial = input("Do you want to specify the material of the product? Answer 'yes' or 'no' ")
    isColor = input("Do you want to specify the color of the product? Answer 'yes' or 'no' ")
    if isMaterial == "yes" and isColor == "yes":
        return "ProductMaterialColor"
    elif isMaterial == "yes" and isColor == "no":
        return "ProductMaterial"
    elif isMaterial == "no" and isColor == "yes":
        return "ProductColor"
    elif isMaterial == "no" and isColor == "no":
        return "Product"
    else:
        print("Please insert yes or no to each question")


class ProductServiceImpl(ProductService):

    def __init__(self):
        self.products = []

    def addProduct(self, name, sku, description, price, stock, images, creationDate, updatingDate, category):
        type = getProductType()
        product = category.createProduct(type)
        product.name = name
        product.sku = sku
        product.description = sku
        product.price = price
        product.stock = stock
        product.images = images
        product.creationDate = creationDate
        product.updatingDate = updatingDate
        print(product)

    def updateProduct(self):
        pass

    def deleteProduct(self):
        pass

    def getProducto(self):
        pass