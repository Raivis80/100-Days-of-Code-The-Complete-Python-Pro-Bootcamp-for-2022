from turtle import Turtle

class Scoreboard(Turtle):
    """
    Scoreboard class

    Methods:
        update_scoreboard: Updates the scoreboard
        l_point: Increases the left score
        r_point: Increases the right score
    """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update_scoreboard method for updating the scoreboard"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """L_point method for increasing the left score"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """R_point method for increasing the right score"""
        self.r_score += 1
        self.update_scoreboard()