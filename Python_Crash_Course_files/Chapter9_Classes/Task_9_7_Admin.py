"""
Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
"""


class User:
    """Class of user of our site"""

    def __init__(self, first_name: str, last_name: str, additional_information: dict = {'age': 18},
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
                 additional_information: dict = {'age': 18}, login_attempts: int = 0,
                 privileges: list = ["can ban user", "can add post", "can delete post"]) -> None:
        super().__init__(first_name, last_name, additional_information, login_attempts)
        self.privileges = privileges

    def show_privileges(self):
        """Shows privileges of this user"""
        print(self.privileges)


user = Admin(first_name='Daniil', last_name="Oliinyk",
             additional_information={})
user.show_privileges()
