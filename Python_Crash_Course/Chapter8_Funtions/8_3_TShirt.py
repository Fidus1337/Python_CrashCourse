"""
T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print a
sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""


def make_shirt(size: str, text_on_the_shirt: str):
    print(f'The shirt is made, its size is {size} ' +
          f'and text on here, as you ordered -  {text_on_the_shirt}')


# calling with positional arguments
make_shirt('M', text_on_the_shirt='Fuck off')

input_size = input('Input size of the shirt: ')
input_text = input('Input text of the shirt: ')
make_shirt(input_size, input_text)  # calling with keyword arguments
