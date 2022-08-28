# Banker Roulette - A game of chance who will pay a bill

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

choice_is = random.choice(names).capitalize()

print(f"{choice_is} is going to buy the meal today!")
