"""
Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize.
"""
import random as rd


def winner_symbols(how_much_symbols_wins: int,
                   symbols_list: list = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']) -> list:
    """Find win symbols"""

    if how_much_symbols_wins > len(symbols_list):
        print("Error")
        return None

    counter = how_much_symbols_wins
    winner_symbols = []
    while (counter != 0):
        rand_number = rd.randint(0, len(symbols_list)-1)
        if symbols_list[rand_number] not in winner_symbols:
            winner_symbols.append(symbols_list[rand_number])
            counter -= 1
    return winner_symbols
