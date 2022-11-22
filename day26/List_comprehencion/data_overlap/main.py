numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

# squared_numbers = [n * n for n in numbers]

#Write your code 👆 above:

# print(squared_numbers)


with open('file1.txt') as file1:
    file1_data = file1.readlines()

with open('file2.txt') as file2:
    file2_data = file2.readlines()

result = [int(n) for n in file1_data if n in file2_data]

# 🚨 Do not change the code below 👇
print(result)

