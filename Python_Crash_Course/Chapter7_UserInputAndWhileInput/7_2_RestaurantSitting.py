"""
Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying they’ll 
have to wait for a table. Otherwise, report that their table is ready
"""
number_of_table = int(input('What is your table? '))
if number_of_table > 8:
    print('You should to wait, sorry')
else:
    print('We have free place')
