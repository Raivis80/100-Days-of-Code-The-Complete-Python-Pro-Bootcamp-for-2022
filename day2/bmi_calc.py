# Body Mass Index calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Add decimal point at index 1 if not present

if height[1] != ".":
    height = height[:1] + "." + height[1:]
    print(height)


# calculate BMI using formula from wikipedia (https://en.wikipedia.org/wiki/Body_mass_index)
BMI = float(weight) / float(height) ** 2


# if BMI is less than 18.5, print "underweight"
if BMI < 18.5:
    print("Your BMI index " + str(int(BMI)) + " wou are underweight\n")
# if BMI is between 18.5 and 25, print "normal"
elif BMI >= 18.5 and BMI <= 25:
    print("Your BMI index " + str(int(BMI)) + " you are normal\n")
# if BMI is between 25 and 30, print "overweight"
elif BMI > 25 and BMI <= 30:
    print("Your BMI index " + str(int(BMI)) + " you are overweight")
# if BMI is greater than 30, print "obese"
elif BMI > 30:
    print("Your BMI index " + str(int(BMI)) + " you are obese")
