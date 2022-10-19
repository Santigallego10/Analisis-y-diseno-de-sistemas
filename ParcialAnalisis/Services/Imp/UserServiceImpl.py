from Services.UserService import UserService
from model.User import User


class UserServiceImpl(UserService):

    def __init__(self):
        self.users = []

    def addUser(self, name, id, address, phoneNumber, email, userType):
        self.users.append(User(name, id, address, phoneNumber, email, userType))

    def updateUser(self, name, id, address, phoneNumber, email, userType, user):


    def deleteUser(self, user):
        pass

    def findUser(self, id):
        for i in self.users:
            if i.id == id:
                return i
        print("There are no users related to the specified id")
