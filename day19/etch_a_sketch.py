from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    """Move the turtle forwards."""
    tim.forward(10)


def move_backwards():
    """Move the turtle backwards."""
    tim.backward(10)


def turn_left():
    """Turn the turtle left."""
    tim.setheading(tim.heading() + 10)


def turn_right():
    """Turn the turtle right."""
    tim.setheading(tim.heading() - 10)


def clear_screen():
    """Clear the screen and reset the turtle to the center."""
    tim.home()
    tim.clear()


screen.listen()
# Higher order functions are functions that can take other functions as arguments.
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
