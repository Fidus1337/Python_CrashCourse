"""
Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store 
all three dictionaries in a list called people. Loop through your list of people. 
As you loop through
the list, print everything you know about each person
"""
general_personal_information = {
    'last_name': 'Week',
    'age': 34,
    'city': 'Lisabon'
}

additional_personal_information = {
    'HasGlasses': False,
    'Hair_color': 'Black',
    'Weight': 45
}

people = {'John': [general_personal_information,
                   additional_personal_information],
          'Filipp': [general_personal_information,
                     additional_personal_information],
          'Joanna': [general_personal_information,
                     additional_personal_information]
          }

for name, person_data in people.items():
    print(f'{name}: {people['Filipp'][0]}; {people['Filipp'][1]}')
