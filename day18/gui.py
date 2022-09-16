from turtle import Turtle, Screen, colormode
import random


colormode(255)

# Create a turtle object
# https://docs.python.org/3/library/turtle.html#turtle.Turtle
tim = Turtle()
tim.shape("turtle")
# https://cs111.wellesley.edu/labs/lab01/colors
tim.color("red")

# # Move square = 4 sides
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# # Inport module Heroes
# import heroes
# print(heroes.gen())

# # Draw a dashed line
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# # Draw a shapes
# def change_color():
#     colors = ["red", "orange", "yellow", "green", "blue", "purple"]
#     return random.choice(colors)
#
#
# def draw_shape(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for side in range(3, 11):
#     draw_shape(side)
#     tim.color(change_color())


# # /////////////////////////////////////////
# # Random walk
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
#
#
# directions = [0, 90, 180, 270]
#
# tim.forward(30)
# tim.setheading(random.choice(directions))
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# /////////////////////////////////////////
# Spirograph
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim.speed('fastest')


def draw_spirograph(size):
    for _ in range(int(360 / size)):
        tim.circle(90)
        tim.setheading(tim.heading() + size)
        tim.color(random_color())

draw_spirograph(10)

# Create a screen object
screen = Screen()
# Set the screen
screen.exitonclick()
