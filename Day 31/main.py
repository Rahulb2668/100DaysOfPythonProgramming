import random
from tkinter import *

import pandas
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME="Ariel"

to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}

## -- Next Card methods --- ##
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=front_card_image)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    learn_data = pandas.DataFrame(to_learn)
    learn_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=back_card_image)

## --- Window Configuration ---##
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(height=526, width=800)

front_card_image = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=front_card_image)
card_title = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 300, text="Word", font=(FONT_NAME, 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

back_card_image = PhotoImage(file="images/card_back.png")



canvas.grid(column=0, row=0, columnspan=2)


# Buttons

right_button_image = PhotoImage(file="images/right.png")
wrong_button_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_button_image, highlightthickness=0 , command=next_card)
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=is_known)

wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)


next_card()
window.mainloop()