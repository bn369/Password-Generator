from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle, random
import json

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

    try:
        with open("data.json", "r") as data_file:
            existing_data = json.load(data_file)
    except FileNotFoundError:
        existing_data = {}

    new_data = {website: {
        "user": user,
        "password": password,
    }}
    is_empty = False
    is_ok = False

    if len(website) == 0 or len(password) == 0 or len(user) == 0:
        messagebox.showinfo(title="Oops!", message="Fields can not be empty")
        is_empty = True
    if not is_empty:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Credentials entered: \nEmail: {user} \nPassword: {password} \n Want to save it?")

    if is_ok and not is_empty:
        existing_data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(existing_data, data_file, indent=4)

            website_entry.delete(0, 'end')
            user_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            print(f"added {website}")
            website_entry.focus()

def find_password():
    search_data = website_entry.get()
    with open("data.json", "r") as data_file:
        try:
            json_data = json.load(data_file)
            for key, value in json_data.items():
                if search_data == key:
                    user = value.get("user")
                    password = value.get("password")
                    messagebox.showinfo(title="search", message=f"{key} \n user: {user} \n password: {password}")
                    return
            # If loop completes without returning, no match was found
            messagebox.showinfo(title="error", message="No data found!")
        except FileNotFoundError:
            messagebox.showinfo(title="error", message="File not found!")
        except json.JSONDecodeError:
            messagebox.showinfo(title="error", message="Invalid JSON format")
        except Exception as e:
            messagebox.showinfo(title="error", message=f"An error occurred: {e}")

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

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")

website_button = Button(text="Search", command=find_password)
website_button.grid(column=2, row=1, sticky="ew")

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
