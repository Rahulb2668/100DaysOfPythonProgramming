import turtle
from turtle import Turtle

import pandas

STATE_GIF_PATH = "blank_states_img.gif"
FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.title("US-State Name Guess Game")

screen.addshape(STATE_GIF_PATH)

turtle.shape(STATE_GIF_PATH)

writer = Turtle()
writer.penup()
writer.hideturtle()

game_not_over = True
data = pandas.read_csv("50_states.csv")

data.state = data.state.str.lower()
state_list = data.state.to_list()
user_guess = []

while len(user_guess) <50:
    answer_state = turtle.textinput(f"{len(user_guess)}/50 Correct Guesses", "Enter your Guess").lower()
    if answer_state == "exit":
        missing_states = []
        for state in state_list:
            if state not in user_guess:
                missing_states.append(state)
        new_df = pandas.DataFrame(missing_states, columns=["Missing States"])
        new_df.to_csv("missing_state.csv")
        break
    if answer_state in state_list and answer_state not in user_guess:
        state_data = data[data.state == answer_state]
        user_guess.append(answer_state)
        writer.goto(int(state_data.x.item()), int(state_data.y.item()))
        writer.write(state_data.state.item(),align="center", font=FONT )

