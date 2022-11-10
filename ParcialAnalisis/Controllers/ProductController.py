from Services.CrudOperation import CrudOperation
from Services.Imp.Product.ProductServiceImpl import ProductServiceImpl
from Services.productServices.ProductLoader import ProductLoader
from FactoryPattern.ProductStore import ProductStore
from FactoryPattern.AccessoryProductStore import AccessoryProductStore
from FactoryPattern.CellphoneProductStore import CellphoneProductStore
from FactoryPattern.ComputerProductStore import ComputerProductStore
from FactoryPattern.DecorativeProductStore import DecorativeProductStore
from FactoryPattern.ElectronicProductStore import ElectronicProductStore
from datetime import date


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
        self.productLoader = ProductLoader("example path")

    def create(self):
        name = input("Write the name of the new product")
        sku = input("Write the SKU")
        description = input("Write a description for the product")
        price = float(input("Write the product's price"))
        stock = int(input("Write how many of this products are available"))
        images = [input("Path for the first Image"),input("Path for the second Image")]
        creationDate = date.today()
        updatingDate = date.today()
        category = self.askCategory()
        self.productService.addProduct(name, sku, description, price, stock, images, creationDate, updatingDate, category)

    def update(self):
        self.productService.updateProduct()

    def detele(self):
        self.productService.deleteProduct()

    def get(self):
        self.productService.getProducto()

    def loadProducts(self):
        self.productLoader.loadProducts()

    def askCategory(self):
        while True:
            option = int(input("To what category does your product belongs?"
                               "\n1.Accessories\n2.Cellphones\n3.Computers\n4.Decoration\n5.Electronics"))
            if option == 1:
                return AccessoryProductStore()
            elif option == 2:
                return CellphoneProductStore()
            elif option == 3:
                return ComputerProductStore()
            elif option == 4:
                return DecorativeProductStore()
            elif option == 5:
                return ElectronicProductStore()
            else:
                print("Please insert a valid option")






