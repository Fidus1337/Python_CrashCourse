def another_function(func):
    """
    A function that accepts another function
    """
    def other_func():
        val = f"{func()} = {eval(func())}"
        return val
    return other_func


def sample_function():
    return "2 + 2"


result = another_function(sample_function)
print(result())  # Выведет: 2 + 2 = 4
