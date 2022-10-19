from Services.Imp.UserServiceImpl import UserServiceImpl
from Services.Imp.WholeSaleBuyer import WholeSaleBuyer
from Services.Imp.OccasionalBuyer import OccasionalBuyer


def askUserType():
    opcion = input("Which user are u?\n1.WholeSale Buyer\n2.Occasional Buyer")
    if opcion == "1":
        return WholeSaleBuyer()
    elif opcion == "2":
        return OccasionalBuyer()
    else:
        print("Please Select a valid option")


class UserController:

    userService: UserServiceImpl

    def __init__(self):
        self.userService = UserServiceImpl()

    def addUser(self):
        name = input("write the name of the new User")
        id = input("Write the id of the user")
        address = input("Write the address of the user")
        phoneNumber = input("Write the phone number of the user")
        email = input("Write the email od the user")
        userType = askUserType()
        self.userService.addUser(name, id, address, phoneNumber, email, userType)

    def updateUser(self):
        user = self.findUserById()

    def deleteUser(self):
        pass

    def findUserById(self):
        id = input("Write the id of the user you want to update")
        return self.userService.findUser(id)
