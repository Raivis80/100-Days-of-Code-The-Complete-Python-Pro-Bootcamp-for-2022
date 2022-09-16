# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.png', 31)
#
# # Create a list of RGB colors.
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# Create a list of colors from an image.
# 100 dots painting, 10 by 10 rows of spots
# Dot 20 in size spaced by 50

import turtle as t
import random

color_list = [(225, 156, 74), (36, 98, 143), (160, 21, 46), (19, 52, 85), (227, 208, 101), (128, 184, 208), (223, 78, 51), (180, 44, 84), (142, 98, 42), (49, 56, 105), (206, 128, 157), (43, 137, 49), (124, 196, 141), (101, 12, 52), (80, 25, 19), (58, 180, 128), (205, 91, 106), (151, 212, 174), (146, 207, 222), (137, 180, 45), (28, 157, 171), (83, 73, 40), (9, 79, 115), (227, 181, 160), (95, 102, 165), (220, 174, 186), (181, 189, 208)]


# Create a screen object
pen = t.Turtle()
t.colormode(255)
pen.penup()
pen.hideturtle()
x = -300
y = -300
start_pos = (x, y)

pen.goto(start_pos)

for i in range(10):
    x = -300
    pen.speed(0)
    pen.goto(x, y)
    y += 60
    for j in range(10):
        pen.speed(10)
        pen.goto(x, y)

        pen.dot(20, random.choice(color_list))
        x += 60


screen = t.Screen()
screen.screensize(600, 600)
# Set the screen
screen.exitonclick()