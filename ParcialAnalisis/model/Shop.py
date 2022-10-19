from Controllers.UserController import UserController
from Controllers.ProductController import ProductController


class Shop:

    '''
    This class owns an instance of the class: UserController and ProductController
    '''

    userController: UserController
    productController: ProductController

    def __init__(self, name):
        self.name = name
        self.userController = UserController()
        self.productController = ProductController()
