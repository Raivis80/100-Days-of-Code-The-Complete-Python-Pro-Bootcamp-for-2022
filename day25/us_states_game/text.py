from turtle import Turtle


class Text(Turtle):

    def __int__(self):
        super().__init__()

    def create_text(self, a, x, y):
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(x, y)
        self.write(a, align='center', font=('Arial', 8, 'normal'))


