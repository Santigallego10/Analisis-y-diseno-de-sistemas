from Services.UserType import UserType


class WholeSaleBuyer(UserType):

    def __init__(self):
        super().__init__()

    def sayHello(self):
        print("We have send you and email ;Do you accept the terms and conditions?")