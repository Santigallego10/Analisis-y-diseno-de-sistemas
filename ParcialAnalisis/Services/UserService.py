from abc import ABC, abstractmethod


class UserService(ABC):

    @abstractmethod
    def addUser(self, name, id, address, phoneNumber, email):
        pass

    @abstractmethod
    def updateUser(self, name, id, address, phoneNumber, email):
        pass

    @abstractmethod
    def deleteUser(self, user):
        pass

    @abstractmethod
    def findUser(self, id):
        pass
