"""
Login Attempts: Add an attribute called login_attempts to your User class
from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""


class User:
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


test_obj = User('Daniil', 'Oliinyk', {'fake_name': 'Fidus', 'age': 18})
print(test_obj.login_attempts)
test_obj.increment_login_attempts()
print(test_obj.login_attempts)
test_obj.reset_login_attempts()
print(test_obj.login_attempts)
