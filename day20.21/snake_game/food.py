from turtle import Turtle, colormode
import time
import random


class Food(Turtle):
    """Create food class"""
    # 1. Create a new class called `Food` that inherits from `Turtle`.
    def __init__(self):
        super().__init__()
        colormode(255)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(self.rand_color())
        self.speed("fastest")
        self.refresh()

    # 2. The `Food` class will need a `shape` and `color` just like the `Snake` class.
    def rand_color(self):
        """Random color"""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    # 3. The `Food` class will also need a `move_food` method that moves the food to a random spot on the screen.
    def refresh(self):
        """Refresh food position"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.color(self.rand_color())