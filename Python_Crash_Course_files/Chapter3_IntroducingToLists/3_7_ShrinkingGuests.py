"""
You just found out that your new dinner table won’t
arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite them
to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program.
"""

def send_message_to_guests(guests_names_arr):
    """The function for sending messages to guests"""
    message_to_send = input("Input your message text: ")
    for name in guests_names_arr:
        print(f"{name}! {message_to_send}")

def delete_guests(guests_names_arr: list[str], guests_to_delete: list[str]):
    """Here we delete guests that will not come"""
    for guest_to_delete in guests_to_delete:
        guests_names_arr.remove(guest_to_delete)
    guests_to_delete.clear() # at this stage we clear delete guests

def check_guests_desire_to_come(guests_names_arr: list[str]):
    """Here we check if each guest from the argument list wants to come"""
    guests_to_delete = [] # This is list of all guests that decided do not come
    for guest in guests_names_arr: # In the cicle we ask each guest if he come
        this_guest_will_come = input(f"Guest {guest} will come?(Yes/No) ")
        match this_guest_will_come:
            case "Yes": # If yes, then we just leave guest in an array
                continue
            case "No": # If no, then we add guest to the delete list
                guests_to_delete.append(guest) 
            case _:
                continue
    if guests_to_delete: # If somebody changed his mind, then we just delete him from our list
        delete_guests(guests_names_arr, guests_to_delete)

def replace_guest(list_of_guest: list[str]):
    """With this function you can replace the old guest with the new one"""
    old_guest = input("Who do you want to replace? ")
    new_guest = input("Who is the new guest? ")
    for index, element in enumerate(list_of_guest):
        if element == old_guest:
            list_of_guest[index] = new_guest
            break

def shrink_guests(list_of_guests: list[str], shrink_to_number: int):
    """Function for shrinking number of guests to fixed value"""
    list_length = len(list_of_guests)
    if shrink_to_number > list_length:
        print("Error shrink_value, it is bigger than length of an input list")
    else:
        while(list_length > 2):
            print(f"{list_of_guests.pop()}, I am sorry, but we cannot invite you :(")
            list_length-=1

guests_names = ["Johnny", "Thomas", "Arthur"] # the list of guests

# leave only 2 guests in the list and let know deleted 
# users that they no longer invited
shrink_guests(guests_names, 2)

send_message_to_guests(guests_names) # send message to guests that are still invited

# delete the last two guests
del guests_names[0] 
del guests_names[0]

print(guests_names)
