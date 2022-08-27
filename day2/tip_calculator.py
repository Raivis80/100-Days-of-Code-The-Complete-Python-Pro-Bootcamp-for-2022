print("Welcome to the tip calculator") # print welcome message

try:
    bill = float(input("What was the total bill?")) # ask for total bill
except ValueError:
    print("Please enter a valid number") # if not a number, print error message
    exit() # exit program
try:
    tip = int(input("What percentage would you like to give? 10, 12 or 15")) # ask for tip percentage
except ValueError:
    print("Please enter a number") # if input is not a number, print error message
    exit() # exit program
try:
    people = int(input("How many people are splitting the bill?")) # ask for number of people splitting the bill
except ValueError:
    print("Please enter a valid number") # if input is not a number, print error message
    exit()
#Each person should pay math formula for bill for each person

tip = int(tip) / 100 # convert tip percentage to decimal
total = float(bill) + (float(bill) * tip) # calculate total bill

print(f"Each person should pay {round(total / int(people), 2)} dollars") # print each person should pay