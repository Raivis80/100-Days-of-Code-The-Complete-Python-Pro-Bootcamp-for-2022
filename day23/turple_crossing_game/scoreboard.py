FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
from turtle import Turtle


class Scoreboard(Turtle):
    """Create a scoreboard.py file that will be responsible
    for keeping score and displaying the current level to the user."""
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard."""
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        """Increase the level."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display game over message."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
