"""
Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.
"""
usernames_list = ['John', 'Joe', 'Jack', 'Johnson', 'Janett', 'admin']
if usernames_list:
    print('We need to find more users')
    for name in usernames_list:
        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello! {name}! How are you?')
