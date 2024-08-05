"""
Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example programs from this chapter,
and extend it by adding new keys and values, changing the context of the program,
or improving the formatting of the output
"""
person_prefers = {
    'favorite_colors': [],
    'favorite_numbers': [],
    'favorite_cities': []
}

person_appearance = {
    'hair_color': '',
    'age': 25,
    'skin_color': '',
    'nationality': ''
}

persons = {
    'Sarah': [person_prefers, person_appearance],
    'John': [person_prefers, person_appearance],
    'Jack': [person_prefers, person_appearance]
}
copy = list(persons.items())
for name, value in copy:
    print(f"{name}: {value[0]}; {value[1]}.\n")
