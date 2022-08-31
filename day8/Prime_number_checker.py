
# check prime number
def prime_checker(number):
    for n in range(2, number-1):
        if number % n == 0:
            return print("It's not a prime number.")
    return print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
