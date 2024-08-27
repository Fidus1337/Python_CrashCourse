"""
Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary
"""
rivers_list = {'nile': 'egypt',
               'amazonka': 'amerika',
               'Missisipi-missuri': 'USA'
               }
rivers_list_temp = list(rivers_list.items())
for river, country in rivers_list_temp:
    if river == 'nile':
        print(f'{river}({country}): The longest river in the world')
    elif river == 'amazonka':
        print(f'{river}({country}): liver located in North Amerika')
    elif river == 'Missisipi-missuri':
        print(f'{river}({country}): main water system in USA')
    else:
        print('ERROR')
