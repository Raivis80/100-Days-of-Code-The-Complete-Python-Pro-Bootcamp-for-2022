# Body Mass Index calculator
try:
    height = float(input("enter your height in m: "))
except ValueError:
    print("invalid input")
    exit('bye')
try:
    weight = float(input("enter your weight in kg: "))
except ValueError:
    print("invalid input")

# Add decimal point at index 1 if not present

if height[1] != ".":
    height = height[:1] + "." + height[1:]
    print(height)


# calculate BMI using formula from wikipedia (https://en.wikipedia.org/wiki/Body_mass_index)
bmi = round(weight / height ** 2)


if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi > 25 and bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
