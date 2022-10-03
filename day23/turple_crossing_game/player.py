STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    """Create a player.py file that will be responsible
    for storing the starting position of the player turtle and
    moving the turtle forward when the "Up" key is pressed."""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        """Move the turtle forward."""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Move the turtle to the starting position."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Return True if the turtle is at the finish line."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
