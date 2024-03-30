import json
import random
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    pass_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)


# -----------------------------Find Password-----------------------------#

def find_password():
    website = web_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")
    else:
        for key, value in data.items():
            if key == website:
                messagebox.showinfo(title=website,
                                    message=f"Username = {data[website]["email"]}\nPassword = {data[website]["password"]}")
            else:
                messagebox.showinfo(title="Oops", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
emuser_label = Label(text="Email/Username:")
emuser_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entry
web_input = Entry(width=21)
web_input.grid(column=1, row=1)
web_input.focus()
email_input = Entry(width=40)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "manish.d3036@gmail.com")
pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

# Buttons
genp_button = Button(text="Generate Password", width=15, command=gen_pass)
genp_button.grid(column=2, row=3)
add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()
