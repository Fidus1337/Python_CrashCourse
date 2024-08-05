"""
Make a list of the numbers from one to one million, and
then use min() and max() to make sure your list actually starts at one and ends
at one million. Also, use the sum() function to see how quickly Python can add
a million numbers.
"""

test_list = list(range(1,1_000_000 + 1))

print(f"Max number: {max(test_list)}")
print(f"Min number: {min(test_list)}")
