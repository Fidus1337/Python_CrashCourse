"""
More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""

print('Car' == 'Car' or 'Car' != 'Machine')  # task 1
print('CAR'.lower() == 'Car'.lower())  # task 2
print((1 == 1 and 1 != 1) or (2 > -9 and 2 < 3) or 2 >= 2 and 2 <= 2)  # task 3
print(True and True or False)  # task 4

test_list = [1, 2, 3, 4, 5]
print(4 in test_list and 6 not in test_list)  # task 5-6
