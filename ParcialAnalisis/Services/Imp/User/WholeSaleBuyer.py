from Services.userServices.UserType import UserType

'''
This class represents an user type
'''
class WholeSaleBuyer(UserType):

    def __init__(self):
        super().__init__()

    def sayHello(self):
        print("We have send you and email ;Do you accept the terms and conditions?")