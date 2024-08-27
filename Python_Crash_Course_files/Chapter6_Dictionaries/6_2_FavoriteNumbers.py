"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
"""
favorite_numbers = {'Sarah': 7, 'John': 9, 'Poll': 1, 'Ronald': 2}
names = list(favorite_numbers.keys())

for person in names:
    print(f"{person}'s favorite number is {favorite_numbers[person]}")
