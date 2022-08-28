import random

# Heads or tails game with a computer
user_input = input("Enter heads or tails: ").lower()

if user_input == "heads":
    print("You chose heads")
    computer_input = random.choice(["heads", "tails"])
    if computer_input == "heads":
        print("The computer chose heads")
        print("You win")
    else:
        print("The computer chose tails")
        print("You lose")
elif user_input == "tails":
    print("You chose tails")
    computer_input = random.choice(["heads", "tails"])
    if computer_input == "tails":
        print("The computer chose tails")
        print("You win")
    else:
        print("The computer chose heads")
        print("You lose")
else:
    print("Invalid input")
