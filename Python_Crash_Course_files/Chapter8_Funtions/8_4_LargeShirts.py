"""
Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""


def make_shirt(size: str = 'large', text_on_the_shirt: str = 'I live Python'):
    print(f'The shirt is made, its size is {size} ' +
          f'and text on here, as you ordered -  {text_on_the_shirt}')


# calling with default arguments
make_shirt()

input_size = input('Input size of the shirt: ')
input_text = input('Input text of the shirt: ')
make_shirt(input_size, input_text)  # calling with keyword arguments
