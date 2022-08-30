# PyPassword generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%','&', '*', '-', '_', '+']

nr_letters = int(input("How many letters do you want in your password?\n"))
nr_numbers = int(input("How many numbers do you want in your password?\n"))
nr_symbols = int(input("How many symbols do you want in your password?\n"))

# generate letter password
password = []
for i in range(nr_letters):
    password.append(random.choice(letters))

# generate number password
for j in range(nr_numbers):
    password.append(random.choice(numbers))

# generate symbol password
for k in range(nr_symbols):
    password.append(random.choice(symbols))

# Shuffle list and convert to string
random.shuffle(password)
password = ''.join(password)

# print password
print(password)

