from art import logo



# Add two numbers
def add(n1, n2):
    return n1 + n2


# Subtract two numbers
def subtract(n1, n2):
    return n1 - n2


# Multiply two numbers
def multiply(n1, n2):
    return n1 * n2


# Divide two numbers
def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(logo)
    continue_calculation = True
    # Ask the user for first number
    num1 = float(input("What's the first number?: "))
    loop_count = 0
    while continue_calculation:
        loop_count += 1
        # print the operations
        for key in operations:
            print(key)
        # Ask the user for an operation
        picked_operation = input("Pick an operation from the line above: ")
        # Ask the user for second number
        num2 = float(input(f"What's the {'second' if loop_count == 1 else 'new'} number?: "))
        # Perform the calculation
        calc_function = operations[picked_operation]
        answer = round(calc_function(num1, num2), 2)

        print(f"{num1} {picked_operation} {num2} = {answer}")
        
        # Ask the user if they want to continue
        question = input(f"Type 'y' to continue calculating with {answer if not answer else num1} or 'n' to start new calculation or 'q' to quit the calculator: ")
        # If the user wants to continue, set the first number to the answer
        if question == 'y':
            continue_calculation = True
            num1 = answer
            answer = ''
        if question == 'n':
            continue_calculation = False
            print("You are restarting the calculation.")
            calculator()
        if question == 'q':
            continue_calculation = False
            print("You are quitting the calculator.")
            break
        else:
            print("Invalid input. Please try again.")

calculator()