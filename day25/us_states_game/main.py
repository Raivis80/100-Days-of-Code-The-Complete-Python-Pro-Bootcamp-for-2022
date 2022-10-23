# Us states game with turtle module
# Guess the state name

import turtle
import pandas

from text import Text

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = ''
states = pandas.read_csv('50_states.csv')
all_states = states.state.to_list()
guessed_states = []


while all_states:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(states)} States left", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        states_to_learn = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv('states_to_learn.csv')

        break
    if answer_state in all_states:
        t = Text()
        t.create_text(answer_state, int(states[states.state == answer_state].x), int(states[states.state == answer_state].y))
        all_states.remove(answer_state)
        guessed_states.append(answer_state)



