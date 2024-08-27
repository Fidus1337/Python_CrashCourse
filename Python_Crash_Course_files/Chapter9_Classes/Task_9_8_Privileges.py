"""
Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""


class Privileges:
    """Class of privileges specific user"""

    def __init__(self, privileges: list = ["can ban user", "can add post", "can delete post"]) -> None:
        self.privileges_list = privileges


class User:
    """Class of user of our site"""

    def __init__(self, first_name: str, last_name: str, additional_information: dict,
                 login_attempts: int = 0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.additional_info = additional_information
        self.login_attempts = login_attempts

    def reset_login_attempts(self):
        """Reset amount of attempts"""
        self.login_attempts = 0

    def increment_login_attempts(self):
        """Increment amount of login attempts"""
        self.login_attempts += 1


class Admin(User):
    """Class of admin, which inherits users class"""

    def __init__(self, first_name: str, last_name: str,
                 additional_information: dict, login_attempts: int = 0,
                 privileges: Privileges = Privileges()) -> None:
        super().__init__(first_name, last_name, additional_information, login_attempts)
        self.privileges = privileges

    def show_privileges(self):
        """Shows privileges of this user"""
        print(self.privileges.privileges_list)


user = Admin(first_name='Daniil', last_name="Oliinyk",
             additional_information={})
user.show_privileges()
