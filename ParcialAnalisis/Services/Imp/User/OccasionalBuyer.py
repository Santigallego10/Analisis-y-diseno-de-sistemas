from Services.userServices.UserType import UserType


class OccasionalBuyer(UserType):

    def __init__(self):
        super().__init__()

    def sayHello(self):
        print("you have successfully registered\n COMING SOON: web catalog of technology products.")
