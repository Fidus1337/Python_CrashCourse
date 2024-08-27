"""
Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
"""

CAR = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(CAR == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(CAR == 'audi')

print("\nTESTS:")
print(CAR == 'subaru' and CAR != 'Audi')  # test 1
print(CAR == 'subaru' and 1 != 'Audi')  # test 2
print(CAR != 'subaruu' or CAR == 'subaru')  # test 3
print(CAR == "sub" + "aru")  # test 4
print(1 + 1 == 3 - 1)  # test 5
print(CAR != CAR)  # test 6
print(CAR == '1')  # test 7
print(CAR == 'arusub')  # test 8
print(CAR == 2)  # test 9
print(CAR == 9)  # test 10
