from Services.userServices.UserType import UserType


class User:

    '''
    This class contains an instance of the class: UserType
    '''

    userType: UserType

    def __init__(self, name, id, address, phoneNumber, email,userType):
        self.name = name
        self.id = id
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email
        self.userType = userType

    """
    This method welcome the new users according to their userType
    """
    def sayHello(self):
        print("User class")
        self.userType.sayHello()




