import random

# Globals
Options = ["R", "P", "S"]
PlayerWins = 0
ComputerWins = 0


# Functions
def validate_input(string):
    if string not in Options:
        raise Exception("Invalid Input")
    else:
        return True


def computer_input():
    random_int = random.randrange(0, 3)
    computer_choice = Options[random_int]
    print("Computer Chose: " + computer_choice)
    return computer_choice


def compare(userinput, computer_choice):
    if userinput == computer_choice:
        return 0
    elif (userinput == "R" and computer_choice == "S") or (userinput == "P" and computer_choice == "R") \
            or (userinput == "S" and computer_choice == "P"):
        return 1
    else:
        return 2


# Call Stack
while True:
    player_input = input("Rock, Paper or Scissors or Q: ")
    if player_input == "Q":
        break
    else:
        validate_input(player_input)
        result = compare(player_input, computer_input())
    if result == 0:
        print("Tie")
    elif result == 1:
        print("Player Wins!")
        PlayerWins += 1
        print("Player Total Wins: " + str(PlayerWins))
        int(PlayerWins)
    elif result == 2:
        print("Computer Wins!")
        ComputerWins += 1
        print("Total Computer Wins: " + str(ComputerWins))
        int(ComputerWins)
