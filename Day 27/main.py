from tkinter import *


def calculate_km():
    input_value = int(user_input.get())
    km_answer.config(text=input_value*1.609)

window = Tk()
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)


user_input = Entry(width=10)
user_input.grid(row=1, column=2)

text = Label()
text.config(text="miles")
text.grid(row=1, column=3)


text_equal = Label()
text_equal.config(text ="is equal to")
text_equal.grid(row=2, column=1)

km_answer = Label()
km_answer.grid(row=2, column=2)

km_text = Label()
km_text.config(text = "kms")
km_text.grid(row=2, column=3)


calculate = Button(text="Calculate", command=calculate_km)
calculate.grid(row=3, column=2)
window.mainloop()