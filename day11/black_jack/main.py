############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from art import logo

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    score = sum(cards)
    # If the score equals 21 and there are only 2 cards, return 0
    if score == 21 and len(cards) == 2:
        return 0
    # If the score is over 21 and there is an Ace, then change the Ace to be a 1 instead of an 11.
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


def compare(user, comp):
    """Compare user and computer score and return the result"""
    if user > 21 and comp > 21:
        return "You went over. You lose 😤"
    if user == comp:
        return "Draw"
    elif user == 0:
        return "You win"
    elif comp == 0:
        return "Computer wins"
    elif user > 21:
        return "You vent over, Computer wins"
    elif comp > 21:
        return "You win"
    elif user < comp:
        return "Computer wins"
    elif user > comp:
        return "You win"

def blackjack():
    """
    Play a game of blackjack
    Loop through the game until the user types 'n' or 'no'
    """
    print(logo)
    game_over = False
    result = ""

    # Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")
            
        # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        # If the game has not ended, ask the user if they want to draw another card.    
        else:
            user_input = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            # If the user types 'y', then deal another card to the user.
            if user_input == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
                
    # Computer draw another card if score is less than 17.            
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
                
    # Output the final scores.
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Compare the user and computer scores and print the result
    result = compare(user_score, computer_score)
    print(result)    
    # Ask the user if they want to restart the game. 
    # #If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
    while input("Do you want to play a new game of Blackjack? Type 'y' or 'n': ") == "y":
        blackjack()
            
blackjack()