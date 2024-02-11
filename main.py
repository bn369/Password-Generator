from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle, random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pw_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)

    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    is_empty = False
    is_ok = False
    if len(website) == 0 or len(password) == 0 or len(user) == 0:
        messagebox.showinfo(title="Oops!", message="Fields can not be empty")
        is_empty = True
    if not is_empty:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Credentials entered: \nEmail: {user} \nPassword: {password} \n Want to save it?")

    if is_ok and not is_empty:
        file = open("data.txt", "a")
        file.write(f"{website} | {user} | {password}\n")
        file.close()
        website_entry.delete(0, 'end')
        user_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="ew")

website_entry = Entry(width=36)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2, sticky="ew")

user_entry = Entry(width=36)
user_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="ew")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")

password_button = Button(text="Generate Password", command=pw_generator)
password_button.grid(column=2, row=3, sticky="ew")

add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()
