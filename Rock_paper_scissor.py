#Rock, Paper, Scissors
from random import randint
import sys
print("-"*147)
print("\t\t\t\t\tRock, Paper, Scissors Game")
print("\t\t\t\t\t","*"*30)
print("\t\t\t\t\tBy Divya Patadiya")
print("-"*147)
print("- Some Instructions to follow while playing the game -")
print("- 1) Enter Proper Choice as displayed as here.")
print("- 2) You will be lost your game as soon as you would enter the wrong choice or miss splled word.")
print("- 3) You may use ctrl+c and type exit() in shell window if you want to quite the game.")
#create a list of play options
t = ["Rock", "Paper", "Scissors"]
#assign a random play to the computer
computer = t[randint(0,2)]
#set player to False
player = False
while player == False:
    #set player to True
    print()
    print("Enter Player Choice:[Rock, Paper, Scissors?]")
    player = input()
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
        print("\n\t\t\t\t\t\tEND GAME\n")
        print("-"*147)
        sys.exit()
#player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
   
    



