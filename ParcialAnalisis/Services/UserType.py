from abc import ABC, abstractmethod


class UserType(ABC):

    @abstractmethod
    def sayHello(self):
        pass



