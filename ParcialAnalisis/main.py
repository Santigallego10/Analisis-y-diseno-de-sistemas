from os import system
from model.User import User
from Controllers.UserController import UserController
from Services.Imp.WholeSaleBuyer import WholeSaleBuyer
from Services.Imp.OccasionalBuyer import OccasionalBuyer


def showUserManagementMenu(userController):
    opcion = input("What you want to do:\n1.Create user\n2.Update User\n3.Delete User\n4.View User details")
    if opcion == "1":
        userController.addUser()
    elif opcion == "2":
        userController.updateUser()
    elif opcion == "3":
        userController.deleteUser()
    elif opcion == "4":
        userController.findUserById()
    else:
        print("You need to select a valid option")

userController = UserController()

print("===========================\nWELCOME TO 'TeLoConsigoStore'\n===========================\n")

while True:

    opcion = input("What you want to do: \n1.Manage Users\n2.Manage Products")
    if opcion == "1":
        showUserManagementMenu(userController)
