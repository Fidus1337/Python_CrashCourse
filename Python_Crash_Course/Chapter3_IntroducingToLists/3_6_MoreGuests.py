"""
You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list
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
    
guests_names = ["Johnny", "Thomas", "Arthur"] # the list of guests

check_guests_desire_to_come(guests_names)

send_message_to_guests(guests_names)

guests_names.insert(0,"Tommy") # the second task

guests_names.insert(3,"Bitch") # the third task

guests_names.append("Bitch3") # the fouth task

send_message_to_guests(guests_names)

print(guests_names)
