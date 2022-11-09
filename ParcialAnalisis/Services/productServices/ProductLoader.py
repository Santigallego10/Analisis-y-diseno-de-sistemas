'''
This class has the responsibility of load products from an Excel file
in his specified pathExcel attribute
'''


class ProductLoader:

    pathExcel: str

    def __init__(self, path):
        self.pathExcel = path

    def loadProducts(self):
        pass
