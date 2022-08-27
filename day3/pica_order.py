print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")

s = ['S', 'M', 'L']
if size.upper() not in s:
    print("Invalid input")
    exit()
add_pepperoni = input("Do you want pepperoni? Y or N ")
y_n = ['Y', 'N', '']
if add_pepperoni.upper() not in y_n:
    print("Invalid input")
    exit()
extra_cheese = input("Do you want extra cheese? Y or N ")
if extra_cheese.upper() not in y_n:
    print("Invalid input")
    exit()
    

size_map = {'S': 15,
            'M': 20,
            'L': 25}

peperoni_s = 2
peperoni_M_L = 3
cheese = 1

bill = 0

bill = size_map[size.upper()]
if add_pepperoni == 'Y':
    if size.upper() == 'M' or size == 'L':
        bill += peperoni_M_L
    else:
        bill += peperoni_s
if extra_cheese.upper() == 'Y':
    bill += cheese

print(f"Your bill is ${bill}")
