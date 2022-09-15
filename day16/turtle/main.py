# from turtle import Turtle, Screen
# # https://docs.python.org/3/library/turtle.html
#
# # Create a turtle object
# timmy = Turtle()
#
# timmy.shape("turtle")
# timmy.color("coral")
#
# # Move the turtle
# timmy.forward(100)
#
# # Create screen object
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

# Create a table object
table = PrettyTable()

# Add columns
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

# Print the table
print(table)