"""
Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.
"""
programming_words = {'highlighting':
                     'this is a way how to make code more readable, by coloring it with defined colours',
                     'list':
                     'this is dynamically created array for storing special values',
                     'dictionary':
                     'this is editing structure that contains pairs "key and value"',
                     'print':
                     'this is function that takes us opportunity to output values in terminal',
                     'line':
                     'in programming is the line where can be located some code'}
temp_list = list(programming_words.items())
for k, v in temp_list:
    print(f"{k} - {v}")
