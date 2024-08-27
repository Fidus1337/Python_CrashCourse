"""Here is the definition of inherited class from user, class Admin"""
from UserModule import *


class Admin(User):
    """Class of admin, which inherits users class"""

    def __init__(self, first_name: str, last_name: str,
                 additional_information: dict = {'age': 18}, login_attempts: int = 0,
                 privileges: list = ["can ban user", "can add post", "can delete post"]) -> None:
        super().__init__(first_name, last_name, additional_information, login_attempts)
        self.privileges = privileges

    def show_privileges(self):
        """Shows privileges of this user"""
        print(self.privileges)
