
import random

# Create a list of play options
options = ["Rock", "Paper", "Scissors"]

# Assign a random play to the computer
computer_choice = random.choice(options)

# Set player to False
player_choice = False

while not player_choice:
    # Set player to True
    player_choice = input("Rock, Paper, or Scissors? ")
    player_choice = player_choice.capitalize()

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "Rock":
        if computer_choice == "Paper":
            print("You lose! Paper covers Rock.")
        else:
            print("You win! Rock smashes Scissors.")
    elif player_choice == "Paper":
        if computer_choice == "Scissors":
            print("You lose! Scissors cut Paper.")
        else:
            print("You win! Paper covers Rock.")
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            print("You lose! Rock smashes Scissors.")
        else:
            print("You win! Scissors cut Paper.")
    else:
        print("That's not a valid play. Please check your spelling!")

    # Set player_choice to False to continue the loop
    player_choice = False
    computer_choice = random.choice(options)