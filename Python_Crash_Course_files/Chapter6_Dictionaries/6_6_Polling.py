"""
Polling: Use the code in favorite_languages.py (page 96).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""
poll_favorite_languages = {'John': 'C', 'Andrey': 'C++', 'Anna': 'Python'}
who_already_passed_poll = list(poll_favorite_languages.keys())

poll_people = ['JOHN', 'AndreY', 'Valentin', 'Sokra']
poll_people_titles = [name.title() for name in poll_people]

for person_name in poll_people_titles:
    if person_name.title() in who_already_passed_poll:
        print(f'Thank you {person_name.title()} for poll!')
    else:
        print(f'{person_name.title()} you still havent passed poll.')
