from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """ScoreBoard class"""
    # 1. Create a `Scoreboard` class that inherits from `Turtle`.
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    # 2. The `Scoreboard` class will need a `score` attribute that starts at 0.
    def update_scoreboard(self):
        """Update scoreboard"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # 3. The `Scoreboard` class will need a `display_score` method that displays the current score on the screen.
    def game_over(self):
        """Game over"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # 4. The `Scoreboard` class will need a `game_over` method that displays "GAME OVER" on the screen.
    def increase_score(self):
        """Increase score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()