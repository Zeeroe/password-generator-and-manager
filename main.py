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
        sep = S.sep
        passphrase = sep.join(rw.get_random_words(
            limit=S.words,
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


def length_f(length):
    S.length = int(length)


length_label = tk.Label(pw_frame, text='Length')
length_label.grid(column=0, row=0)
length_scale = tk.Scale(pw_frame, from_=4, to=32, orient=tk.HORIZONTAL, command=length_f)
length_scale.set(16)
length_scale.grid(column=1, row=0)


class Checkbox:
    def __init__(self, lt, g, sub, add):
        self.lt = lt    # Label Text
        self.g = g      # Grid Row
        self.sub = sub  # Characters to remove (Regex)
        self.add = add  # Characters to add

        self.label = tk.Label(pw_frame, text=self.lt).grid(column=0, row=g)
        self.var = tk.IntVar(pw_frame)
        self.check = tk.Checkbutton(pw_frame, variable=self.var, command=self.func)
        self.check.grid(column=1, row=g)
        self.check.invoke()

    def func(self):
        if self.var.get() == 0:
            S.characters = re.sub(self.sub, '', S.characters)
        elif self.var.get() == 1:
            S.characters += self.add


low = Checkbox('a-z', 1, '[a-z]', 'abcdefghijklmnopqrstuvwxyz')
up = Checkbox('A-Z', 2, '[A-Z]', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num = Checkbox('0-9', 3, '[0-9]', '0123456789')
sym = Checkbox('!@#$%^&*', 4, '[!@#$%^&*]', '!@#$%^&*')

# Passphrase Frame
pp_frame = tk.Frame(root)
pp_frame.grid(column=0, row=4)


# Dropdown Menu
def switch_mode(v):
    print(v)


mode_list = ['Password', 'Passphrase']
mode_str = tk.StringVar(root, value='Password')
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
