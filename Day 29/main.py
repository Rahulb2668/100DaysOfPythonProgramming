from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- GENERATE PASSWORD ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbols + password_numbers

    random.shuffle(password_list)

    password_gen = "".join(password_list)
    password_entry.insert(0, password_gen)
    pyperclip.copy(password_gen)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# Submit Function
def save_to_text():

    website_value = website.get().strip()
    password_value = password.get().strip()
    username_value = username.get().strip()


    if len(website_value) == 0:
        messagebox.showinfo(title="Invalid Data", message="Website Field Cannot be empty")
        return
    if len(password_value) == 0:
        messagebox.showinfo( title="Invalid Data", message="Password Field Cannot be empty")
        return

    is_ok = messagebox.askokcancel(title=website_value, message=f"These are details Entered:\n Email: {username_value} \n Password: {password_value}.\n Is it ok to save?")
    if not is_ok:
        return
    with open("my_password.txt", "a") as file:
        file.write(f"{website_value} | {username_value} | {password_value}\n")
        website_name_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# Configuring the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


#Variable Configuration
website = StringVar()
username = StringVar()
password=StringVar()



# Configure column weights for proper stretching
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=0)

# Configuring the canvas
canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website", anchor="e")
email_or_username_label = Label(text="Email/UserName", anchor="e")
password_label = Label(text="Password", anchor="e")

website_label.grid(column=0, row=1)
email_or_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entries
website_name_entry = Entry(textvariable=website)
website_name_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_name_entry.focus()

email_entry = Entry(textvariable=username)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "rahulb2668@gmail.com")

password_entry = Entry(textvariable=password)
password_entry.grid(row=3, column=1, sticky="ew")

# Buttons
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(row=3, column=2, sticky="ew")

# Save button
add_password_button = Button(text="Save", command=save_to_text)
add_password_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
