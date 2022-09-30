from turtle import Turtle


class Paddle(Turtle):
    """
    Paddle class

    Methods:
        up: Moves the paddle up
        down: Moves the paddle down
    """
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        """Up method for moving the paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        """Down method for moving the paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)