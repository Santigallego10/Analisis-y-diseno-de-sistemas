from Services.CrudOperation import CrudOperation
from Services.Imp.Product.ProductServiceImpl import ProductServiceImpl
from Services.productServices.ProductLoader import ProductLoader


class ProductController(CrudOperation):

    productService: ProductServiceImpl
    productLoader: ProductLoader

    def __init__(self):
        self.productService = ProductServiceImpl()
        self.productLoader = ProductLoader()

    def create(self):
        self.productService.addProduct()

    def update(self):
        self.productService.updateProduct()

    def detele(self):
        self.productService.deleteProduct()

    def get(self):
        self.productService.getProducto()

    def loadProducts(self):
        self.productLoader.loadProducts()
