"""
10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop
so the user can continue entering numbers, even if they make a mistake and
enter text instead of a number
"""
while True:
    value1 = input("Input first number: ")
    value2 = input("Input second number: ")
    try:
        result = int(value1) + int(value2)
    except ValueError:
        print("You have input non-numerical symbol")
    else:
        print(result)
