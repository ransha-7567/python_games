import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

guess_number()

""" Review of Content
- The guess_number() function is defined to encapsulate the game logic.
- The random.randint() function is used to generate a random number.
- The attempts variable keeps track of the number of attempts made by the player.
- The try-except block handles invalid input if the player enters something other than an integer.
- The game provides appropriate feedback for each guess, indicating whether it is too high or too low.
- Once the player guesses the correct number, the game ends and displays the number of attempts made.
- The guess_number() function is called at the end to start the game.

Hours Spent on Code: 3

"""