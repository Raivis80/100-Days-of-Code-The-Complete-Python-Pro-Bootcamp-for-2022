from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """ScoreBoard class"""
    # `Scoreboard` class that inherits from `Turtle`.
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    # The `Scoreboard` class will need a `score` attribute that starts at 0.
    def update_scoreboard(self):
        """Update scoreboard"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # The `Scoreboard` class will need a `high_score` attribute that starts at 0.
    def reset(self):
        """Reset score"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # The `Scoreboard` class will need a `display_score` method that displays the current score on the screen.
    def game_over(self):
        """Game over"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # The `Scoreboard` class will need a `game_over` method that displays "GAME OVER" on the screen.
    def increase_score(self):
        """Increase score"""
        self.score += 1
        self.update_scoreboard()