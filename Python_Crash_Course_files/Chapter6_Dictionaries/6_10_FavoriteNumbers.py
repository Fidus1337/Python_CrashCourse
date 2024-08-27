"""
Modify your program from Exercise 6-2 (page 98) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""

favorite_numbers = {
    'Sarah': [7, 2, 4],
    'John': [7, 2, 4],
    'Poll': [7, 2, 4],
    'Ronald': [7, 2, 4]
}
names = list(favorite_numbers.keys())

for person in names:
    print(f"{person}'s favorite number is {favorite_numbers[person]}")
