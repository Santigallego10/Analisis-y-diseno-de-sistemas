from Services.UserType import UserType


class User:

    userType: UserType

    def __init__(self, name, id, address, phoneNumber, email,userType):
        self.name = name
        self.id = id
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email
        self.userType = userType

    def sayHello(self):
        print("User class")
        self.userType.sayHello()




