"""
Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
"""
input_value = int(input('Input value that is multiplie of ten '))
if input_value % 10 == 0:
    print('Yes, it is multiplie of ten')
else:
    print('Wrong symbol or it is not multiplie of ten')
