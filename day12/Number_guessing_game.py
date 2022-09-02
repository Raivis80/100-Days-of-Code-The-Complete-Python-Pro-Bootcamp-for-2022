from art import logo
import random

EASY_LEVEL_TURNS = 5
HARD_LEVEL_TURNS = 10

# set the difficulty level
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        turns = EASY_LEVEL_TURNS
    elif difficulty == 'hard':
        turns = HARD_LEVEL_TURNS
    else:
        print("Invalid input. Please try again.")

    return turns

# Check if the user's guess is correct
def check_answer(guess, answer, turns):
    """Check if the user's guess is correct and returns turns"""
    if guess > answer:
        print("Your guess is too high.")
        return turns - 1
    elif guess < answer:
        print("Your guess is too low.")
        return turns - 1
    else:
        print(f"You guessed the number! The number was {answer}.")

def game():
    # Choice a random number between 1 and 100
    print(f"{logo}\nWelcome to the Number Guessing Game!\n"
            "I'm thinking of a number between 1 and 100.")
    # generate a random number
    answer = random.randint(1, 100)

    # set the number of turns
    turns = set_difficulty()


    # repeat until the user guesses the number or runs out of turns
    guess = 0
    while guess != answer:
        print(f"You have {turns} lives remaining.")
        # ask the user to guess the number
        guess = int(input("Make a guess: "))
        # check if the user's guess is correct
        # return the number of turns remaining
        turns = check_answer(guess, answer, turns)
        
        # if the user runs out of turns, end the game
        if turns == 0:
            print(f"You ran out of lives. The number was {answer}.")
            return
game()

if input("Would you like to play again? (y/n): ").lower() == 'y':
    game()



