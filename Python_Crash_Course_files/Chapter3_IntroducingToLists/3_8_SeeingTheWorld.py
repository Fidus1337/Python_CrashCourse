"""
Think of at least five places in the world you’d like
to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly;
just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the
actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show that its
order has changed.
• Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed
"""

cities_list = ["Paris", "London", "Berlin", "Bern", "Kiev"] # first task

print(f"2)Using sorted() function for alphabetic sorting:\n{sorted(cities_list, reverse=False)}\n") # second task

print(f"3)The source list is still the same: \n{cities_list}\n") # third task

print(f"4)Using sorted() function for reverse-alphabetic sorting: \n{sorted(cities_list, reverse=True)}\n") # fourth task

print(f"5)The source list is still the same: \n{cities_list}\n") # fiveth task

cities_list.reverse() # sixth task (here we are changing the list with reverse method)

print(f"6)Source list has changed: \n{cities_list}\n") # sixth task (here we are showing our changed list)

cities_list.reverse() # seventh task (we are using reverse method again)

print(f"7)Source list has changed: \n{cities_list}\n") # seventh task (here we are showing our changed list)

cities_list.sort(reverse=False) # eighth task (we are sorting our list in alphabetical order)

print(f"8)Source list has changed: \n{cities_list}\n") # eighth task (here we are showing our changed list)

cities_list.sort(reverse=True) # nineth task (we are sorting our list in reverse-alphabetical order)

print(f"Source list has changed: \n{cities_list}\n") # eighth task (here we are showing our changed list)