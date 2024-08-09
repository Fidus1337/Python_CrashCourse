"""
One excellent resource for exploring the
Python standard library is a site called Python Module of the Week. Go to
https://pymotw.com and look at the table of contents. Find a module that looks
interesting to you and read about it, perhaps starting with the random module.

I have chosen time module
"""
import time

template = '{} - {:0.2f} - {:0.2f}'

print(template.format(
    time.ctime(), time.time(), time.process_time())
)

for i in range(3, 0, -1):
    print('Sleeping', i)
    time.sleep(i)
    print(template.format(
        time.ctime(), time.time(), time.process_time())
    )
