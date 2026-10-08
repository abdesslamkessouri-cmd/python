import sys
from random import choice
from enum import Enum
class RPS(Enum):
    Rock = 1
    Paper = 2
    scissors = 3



print()

player_choice= int(input("Please Enter your choice\n1 for rock\n2 for Paper\n3 for sessores\n"))

if player_choice <1 or player_choice >3:
    sys.exit("You must Enter 1, 2 or 3")

computer_choice = int(choice("123"))

print("Player choice: "+str(RPS(player_choice).name))
print("computer choice: "+str(RPS(computer_choice)).replace("RPS.",""))


#if player_choice == 1:
#   print("Player choice: Rock")
#elif player_choice == 2:
#    print("Player choice: Paper")
#else:
#    print("Player choice: sessors")


#if computer_choice == 1:
#    print("computer_choice: Rock")
#elif computer_choice == 2:
#    print("computer choice: Paper")
#else:
#    print("computer choice: sessors")

if player_choice == computer_choice:
    print("draw")
elif player_choice == 1 and computer_choice == 3:
    print("Player wins")
elif player_choice == 2 and computer_choice == 1:
    print("Player wins")
elif player_choice == 3 and computer_choice == 2:
    print("Player wins")
else:
    print("Computers wins")