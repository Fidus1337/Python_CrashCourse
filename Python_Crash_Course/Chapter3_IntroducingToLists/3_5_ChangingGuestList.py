"""
You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in
your list.
"""

def send_invites(guests_names_arr):
    """The function for sending invitations"""
    for name in guests_names_arr:
        print(f"{name}! We will wait for you at 9 pm tomorrow. We have swab.")

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
send_invites(guests_names)

check_guests_desire_to_come(guests_names)

send_invites(guests_names)

replace_guest(guests_names)

print(guests_names)





