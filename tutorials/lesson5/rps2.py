import sys
from random import choice
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

player_choice = int(input("Please Enter your choice:\n1 for ROCK\n2 for Paper\n3 for Scissors\n"))

if player_choice > 3 or player_choice < 1:
    sys.exit("You need to enter an integer between 1 and 3")

computer_choice = int(choice("123"))

print("Player choice:",RPS(player_choice).name)
print("Computer choice:",RPS(computer_choice).name)


