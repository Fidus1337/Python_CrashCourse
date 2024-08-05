"""
Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user.
• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.
"""
usernames_list = ['John', 'Joe', 'Jack', 'Johnson', 'Janett', 'admin']
for name in usernames_list:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello! {name}! How are you?')
