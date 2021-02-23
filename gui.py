import tkinter as tk
from settings import Settings
import random, random_word, re

S = Settings()
rw = random_word.RandomWords()


def gen_word():
    try:
        password = ''.join(random.choice(S.characters) for _ in range(S.length))
    except IndexError:
        password = ''
    pw_entry.delete(0, len(pw_entry.get()))
    pw_entry.insert(1, password)


def gen_phrase():
    try:
        passphrase = S.separator.join(rw.get_random_words(limit=S.words,
                                                          minLength=S.minlength,
                                                          maxLength=S.maxlength,
                                                          hasDictionaryDef='True'))

        passphrase = passphrase.title()
        pw_entry.delete(0, len(pw_entry.get()))
        pw_entry.insert(1, passphrase)

    except TypeError:
        print('TypeError')
        gen_phrase()


# Window
root = tk.Tk()
root.title("1Pass")
root.geometry('300x400')

# Text
pw_entry = tk.Entry(root, width=50, justify=tk.CENTER)
pw_entry.grid(column=0, row=0)

# Settings Label
settings_label = tk.Label(text='Settings')
settings_label.grid(column=0, row=2)

# Password Frame
pw_frame = tk.Frame(root)
pw_frame.grid(column=0, row=4)


def low_f():
    if low_var.get() == 0:
        S.characters = re.sub('[a-z]', '', S.characters)
    elif low_var.get() == 1:
        S.characters += 'abcdefghijklmnopqrstuvwxyz'


low_label = tk.Label(pw_frame, text='a-z')
low_label.grid(column=0, row=0)
low_var = tk.IntVar(pw_frame)
low_check = tk.Checkbutton(pw_frame, variable=low_var, command=low_f)
low_check.grid(column=1, row=0)


def up_f():
    if up_var.get() == 0:
        S.characters = re.sub('[A-Z]', '', S.characters)
    elif up_var.get() == 1:
        S.characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


up_label = tk.Label(pw_frame, text='A-Z')
up_label.grid(column=0, row=1)
up_var = tk.IntVar(pw_frame)
up_check = tk.Checkbutton(pw_frame, variable=up_var, command=up_f)
up_check.grid(column=1, row=1)


def num_f():
    if num_var.get() == 0:
        S.characters = re.sub('[0-9]', '', S.characters)
    elif num_var.get() == 1:
        S.characters += '0123456789'


num_label = tk.Label(pw_frame, text='0-9')
num_label.grid(column=0, row=2)
num_var = tk.IntVar(pw_frame)
num_check = tk.Checkbutton(pw_frame, variable=num_var, command=num_f)
num_check.grid(column=1, row=2)


def sym_f():
    if sym_var.get() == 0:
        S.characters = re.sub('[!@#$%^&*]', '', S.characters)
    elif sym_var.get() == 1:
        S.characters += '!@#$%^&*'


sym_label = tk.Label(pw_frame, text='!@#$%^&*')
sym_label.grid(column=0, row=3)
sym_var = tk.IntVar(pw_frame)
sym_check = tk.Checkbutton(pw_frame, variable=sym_var, command=sym_f)
sym_check.grid(column=1, row=3)

# Passphrase Frame
pp_frame = tk.Frame(root)
pp_frame.grid(column=0, row=4)


# Dropdown Menu
def switch_mode(v):
    print(v)


mode_list = ['Password', 'Passphrase']
mode_str = tk.StringVar(root)
mode_drop = tk.OptionMenu(root, mode_str, *mode_list, command=switch_mode)
mode_drop.grid(column=0, row=3)


def generate():
    if mode_str.get() == 'Password':
        gen_word()
    elif mode_str.get() == 'Passphrase':
        gen_phrase()


generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.grid(column=0, row=1)

root.mainloop()
