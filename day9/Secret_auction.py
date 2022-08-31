from art import logo
# bidders = []
# bidding = True

# # Function To return the highest bidder

# def get_highest_bidder():
#     highest_bidder = {'name': None, 'bid': 0}
#     if len(bidders) > 0:
#        for i in bidders:
#            if i['bid'] > highest_bidder['bid']:
#                highest_bidder = i
#     return print(f" Highest bidder is {highest_bidder['name']} with bid {highest_bidder['bid']}")


# # Bidding loop - keep asking for bids until the bidding is over
# while bidding:
#     name = input("What is your name? ")

#     #Loop until the user enters a valid bid
#     is_bid: bool = False
#     while not is_bid:
#         try:
#             bid = int(input("What is your bid? "))
#             is_bid = True
#         except ValueError:
#             print("That is not a valid bid. Please enter a number.")

#     user = {"name": name, "bid": bid}
#     bidders.append(user)

#     # Loop to Ask if there is another bidder
#     is_answer: bool = False
#     while not is_answer:
#         question = input("Is there any other bidder? (y/n) ")
#         if question == "n":
#             bidding = False
#             is_answer = True
#         elif question == "y":
#             is_answer = True
#         else:
#             print("Invalid input")


# get_highest_bidder()


print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)

