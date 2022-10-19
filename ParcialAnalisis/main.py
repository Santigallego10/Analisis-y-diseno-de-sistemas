from Controllers.UserController import UserController
from model.Shop import Shop


def showUserManagementMenu(userController):
    opcion = input("What you want to do:\n1.Create user\n2.Update User\n3.Delete User\n4.View User details")
    if opcion == "1":
        userController.create()
    elif opcion == "2":
        userController.update()
    elif opcion == "3":
        userController.detele()
    elif opcion == "4":
        userController.get()
    else:
        print("You need to select a valid option")


shop = Shop("TeLoConsigo")

print("===========================\nWELCOME TO 'TeLoConsigoStore'\n===========================\n")

while True:

    opcion = input("What you want to do: \n1.Manage Users\n2.Manage Products")
    if opcion == "1":
        showUserManagementMenu(shop.userController)
