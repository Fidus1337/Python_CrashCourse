"""Here is the definition of User Class"""


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
