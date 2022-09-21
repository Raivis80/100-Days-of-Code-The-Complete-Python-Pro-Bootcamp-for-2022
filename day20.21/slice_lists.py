piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
piano_keys_tuple = tuple(piano_keys)
print(piano_keys_tuple)

# Slicing lists and tuples in Python

# 1. Create a variable called `first_four` that is a slice of the first four items in `piano_keys`.
first_four = piano_keys[:4]
print(first_four)

# 2. Create a variable called `last_three` that is a slice of the last three items in `piano_keys`.
last_three = piano_keys[-3:]
print(last_three)

# 3. Create a variable called `middle_six` that is a slice of the middle six items in `piano_keys`.
middle_six = piano_keys[10:16]
print(middle_six)

# 4. Create a variable called `reverse` that is a slice of all the items in `piano_keys` in reverse order.
reverse = piano_keys[::-1]
print(reverse)

# 5. Create a variable called `every_other` that is a slice of every other item in `piano_keys`.
every_other = piano_keys[::2]
print(every_other)

# 6. Create a variable called `every_other_reversed` that is a slice of every other item in `piano_keys` in reverse order.
every_other_reversed = piano_keys[::-2]
print(every_other_reversed)
