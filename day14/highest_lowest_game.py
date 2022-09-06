# TODO:1 import data, logo, random
import random
from art import logo, vs
from game_data import data

#display art


def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = get_random_account()


#TODO:5 Score keeping
while game_should_continue:
    #TODO:7 Making account at position B become the next account at position A
    account_a = account_b
    account_b = get_random_account()
    
    while account_a == account_b:
        account_b = get_random_account()
        
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #TODO:2 Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #TODO:3 Check if user is correct

    ## Get follower count of each account
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]
    ## Use if statement to check if user is correct
    is_correct = check_answer(guess, a_followers_count, b_followers_count)


    #TODO:4 Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You got it right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"You got it wrong! Finale score: {score}")






