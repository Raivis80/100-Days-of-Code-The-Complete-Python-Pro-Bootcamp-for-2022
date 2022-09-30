from turtle import Turtle
from random import randint


class Ball(Turtle):
    """
    Ball class

    Methods:
        move: Moves the ball
        bounce_y: Bounces the ball off the wall
        bounce_x: Bounces the ball off the paddle
        reset_position: Resets the ball position
        random_angle: Gives the ball a random angle
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Move method for moving the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounce_y method for bouncing the ball off the wall"""
        self.y_move *= -1

    def bounce_x(self):
        """Bounce_x method for bouncing the ball off the paddle"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset_position method for resetting the ball position"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def random_angle(self):
        """Random_angle method for giving the ball a random angle"""
        self.x_move = randint(10, 20)
        self.y_move = randint(10, 20)
        self.move_speed = 0.1
        self.bounce_x()