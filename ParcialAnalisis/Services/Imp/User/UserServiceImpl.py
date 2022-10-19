from Services.userServices.UserService import UserService
from model.User import User

'''
This class implements the interface UserService 
This class owns the list of users
'''


class UserServiceImpl(UserService):

    def __init__(self):
        self.users = []

    '''
    This method receives all the parameters needed to create and user.
    This method create a new user and add it to the list
    '''
    def addUser(self, name, id, address, phoneNumber, email, userType):
        self.users.append(User(name, id, address, phoneNumber, email, userType))

    '''
    This method receives all the parameters needed to update and user, including the User that
     it wants to be updated.
    '''
    def updateUser(self, name, id, address, phoneNumber, email, userType, user):
        pass

    '''
    This method receives and user and delete it
    '''
    def deleteUser(self, user):
        pass

    '''
    This method receives and id and return a user that match.
    If user doesnt exits throws an alert
    '''
    def findUser(self, id):
        for i in self.users:
            if i.id == id:
                return i
        print("There are no users related to the specified id")

