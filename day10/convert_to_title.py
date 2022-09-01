
# define function to convert string to title case
def to_title_case(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


name = input("Enter your name: ")
lastname = input("Enter your lastname: ")

# Call the function and print the result
formated_name = to_title_case(name, lastname)
print(formated_name)
