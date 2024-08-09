"""
You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write
a loop that keeps pulling numbers until your ticket wins. 
Print a message reporting how many times the loop had to run to give you a winning ticket.
"""
from Task_9_14_Lottery import winner_symbols

lottery_numbers: list = [
    '1', '2', '3', '4',
    '5', 'a', 'b', 'c',
    'd', 'e', '8', '9',
    '0', 'l', 'g', '('
]

chosen_symbol = input("What symbol do you want to choose: ")

win_symbols = None
tries_counter = 0
while chosen_symbol != win_symbols:
    tries_counter += 1
    win_symbols = winner_symbols(1, lottery_numbers)
    if chosen_symbol in win_symbols:
        print(f"You have won! You have spent {tries_counter} tries")
        break
    else:
        print(f"You have lost! The win symbol is - {win_symbols}")
