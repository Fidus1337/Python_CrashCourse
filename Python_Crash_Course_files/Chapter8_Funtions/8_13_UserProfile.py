"""
User Profile: Start with a copy of user_profile.py from page 148. Build a
profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
"""


def describe_person(first_name: str, last_name: str, **additional_details):
    print(f"His/her name is {first_name} and the last name {last_name}")
    for info_key, info_value in additional_details.items():
        print(f"{info_key}:{info_value}")


describe_person('Danii', 'Oliinyk',
                age=18,
                location='Czech')
