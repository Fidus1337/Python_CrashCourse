"""
Make a class Die with one attribute called sides, which has a
default value of 6. Write a method called roll_die() that prints a random number 
between 1 and the number of sides the die has. Make a 6-sided die and
roll it 10 times.
"""
from random import randint


class Dice:
    def __init__(self, number_of_sides: int) -> None:
        self.sides: int = number_of_sides

    def roll_dice(self):
        print(randint(1, self.sides))


dice1 = Dice(6)
dice1.roll_dice()

print("Start rolling:")
counter = 0
while (counter != 10):
    dice1.roll_dice()
    counter += 1
