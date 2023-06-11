import time

def start_game():
    print("Welcome to the Adventure Game!")
    print("You wake up in a mysterious room. Your goal is to escape.")
    time.sleep(2)
    print("\nYou find three doors in front of you labeled A, B, and C.")
    chosen_door = input("Which door do you choose? (A, B, or C): ").upper()
    if chosen_door == 'A':
        room_a()
    elif chosen_door == 'B':
        room_b()
    elif chosen_door == 'C':
        room_c()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def room_a():
    print("\nYou enter Room A.")
    print("In the room, you see a table with a key on it.")
    time.sleep(2)
    print("\nWhat would you like to do?")
    choice = input("1. Take the key\n2. Go back to the main room\nEnter your choice (1 or 2): ")
    if choice == '1':
        print("\nYou took the key and returned to the main room.")
        start_game()
    elif choice == '2':
        print("\nYou went back to the main room.")
        start_game()
    else:
        print("\nInvalid choice. Please try again.")
        room_a()

def room_b():
    print("\nYou enter Room B.")
    print("In the room, you see a locked door.")
    time.sleep(2)
    print("\nWhat would you like to do?")
    choice = input("1. Try the key from Room A\n2. Go back to the main room\nEnter your choice (1 or 2): ")
    if choice == '1':
        print("\nYou use the key you found in Room A to unlock the door!")
        print("Congratulations! You escaped the room.")
    elif choice == '2':
        print("\nYou went back to the main room.")
        start_game()
    else:
        print("\nInvalid choice. Please try again.")
        room_b()

def room_c():
    print("\nYou enter Room C.")
    print("In the room, you see a chest.")
    time.sleep(2)
    print("\nWhat would you like to do?")
    choice = input("1. Open the chest\n2. Go back to the main room\nEnter your choice (1 or 2): ")
    if choice == '1':
        print("\nYou open the chest and find a hidden passage!")
        print("You enter the passage and find yourself outside the room.")
        print("Congratulations! You escaped the room.")
    elif choice == '2':
        print("\nYou went back to the main room.")
        start_game()
    else:
        print("\nInvalid choice. Please try again.")
        room_c()

start_game()


""" Review of Content
- Start the Game: The start_game() function serves as the entry point for the game. 
It displays the initial welcome message, introduces the objective of the game, and 
presents the player with three doors to choose from (A, B, and C). 
The input() function is used to get the player's choice, and the if-elif-else 
statement is used to handle different door choices.

- Room A: The room_a() function represents the actions and choices in Room A. 
In this room, the player sees a table with a key on it. The input() function is used to prompt 
the player for their choice: to take the key or go back to the main room. 
Based on their choice, the function calls either start_game() or room_a() recursively to continue the game flow.

- Room B: The room_b() function represents the actions and choices in Room B. 
In this room, the player encounters a locked door. Again, the input() function is used to prompt the player for their 
choice: to try the key from Room A or go back to the main room. Based on their choice, 
the function either congratulates the player for escaping or calls start_game() or room_b() recursively.

- Room C: The room_c() function represents the actions and choices in Room C. 
In this room, the player finds a chest. The input() function prompts the player for their choice: 
to open the chest or go back to the main room. Based on their choice, the function either 
congratulates the player for escaping or calls start_game() or room_c() recursively.

- Input Validation: Throughout the program, input validation is implemented to handle invalid choices. 
If the player enters an invalid choice, an appropriate message is displayed, and the corresponding function 
(start_game(), room_a(), room_b(), or room_c()) is called again to allow the player to make a valid choice.

- Time Delays: The time.sleep() function is used to introduce delays at certain points in the game. 
This provides a more realistic and immersive experience for the player, giving them time to read the prompts and 
messages.

Hours Spent on Code: 8

"""