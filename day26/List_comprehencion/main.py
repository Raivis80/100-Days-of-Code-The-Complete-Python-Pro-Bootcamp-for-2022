
# List comprehensions are a way to create lists in a single line of code
# They are a way to create a new list from an existing list

# Example 1
# Create a new list with the first letter of each word in a string
words = "What is the Airspeed Velocity of an Unladen Swallow?".split()
print(words)

# Create a new list with the first letter of each word in a string
# Using a for loop
first_letters = []
for word in words:
    first_letters.append(word[0])
print(first_letters)

# Create a new list with the first letter of each word in a string
# Using a list comprehension
first_letters = [word[0] for word in words]
print(first_letters)

# Example 2
# Create a new list with the numbers from 1 to 5
# Add 1 to each number in the list using a list comprehension

numbers = [1, 2, 3, 4, 5]
new_numbers = [n + 1 for n in numbers]

print(new_numbers)

# Example 3
# Create a word
# return a new list with the letters in the word

word = "Hello"
new_list = [letter for letter in word]
print(new_list)

# Example 4
# Create a list of numbers range 1 to 4 using range()
# Create a new list with the numbers from the first list multiplied by 2

numbers = range(1, 5)
new_numbers = [n * 2 for n in numbers]
print(new_numbers)

# Example 5
# Create conditional list comprehensions with if statements
# Create a list of names
# Create a new list with only names with length of 4 or less

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_names = [n for n in names if len(n) <= 4]
print(new_names)

# Example 6
# Turn this names list into a uppercase list
new_names = [n.upper() for n in names if len(n) <= 5]
print(new_names)
