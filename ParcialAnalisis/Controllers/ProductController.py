from Services.CrudOperation import CrudOperation
from Services.Imp.Product.ProductServiceImpl import ProductServiceImpl
from Services.productServices.ProductLoader import ProductLoader

'''
This class manage the data inputs related to the Class: Product

This class sends all data inputs to his instance of the class: ProductService
'''


class ProductController(CrudOperation):
    productService: ProductServiceImpl
    productLoader: ProductLoader

    def __init__(self):
        '''
        Initializes productService and productLoader in order to have a singular instance
        '''
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
