import tkinter as tk
from settings import Settings
import random
import random_word
import re

S = Settings()
rw = random_word.RandomWords()


def gen_word():
    try:
        password = ''.join(random.choice(S.characters) for _ in range(S.length))
    except IndexError:
        password = ''
    text_entry.delete(0, len(text_entry.get()))
    text_entry.insert(1, password)


def gen_phrase():
    try:
        sep = S.sep
        g = rw.get_random_words(
            limit=S.words,
            minLength=S.minlength,
            maxLength=S.maxlength)
        # g.insert(random.randrange(1, len(g)), random.randint(1, 9))
        passphrase = sep.join(g)

        if S.casing == 'lower':
            passphrase = passphrase.lower()
        elif S.casing == 'upper':
            passphrase = passphrase.upper()
        elif S.casing == 'title':
            passphrase = passphrase.title()

        text_entry.delete(0, len(text_entry.get()))
        text_entry.insert(0, passphrase)

    except TypeError:
        print('TypeError')
        gen_phrase()


# Window
root = tk.Tk()
root.title("1Pass")
root.geometry('300x400')

text_entry = tk.Entry(root, width=50, justify=tk.CENTER)
text_entry.grid(column=0, row=0)

settings_label = tk.Label(text='Settings')
settings_label.grid(column=0, row=2)


# Dropdown Menu
def switch_mode(mode):
    if mode == 'Passphrase':
        pw_frame.grid_forget()
        pp_frame.grid(column=0, row=4)
        gen_phrase()
    elif mode == 'Password':
        pp_frame.grid_forget()
        pw_frame.grid(column=0, row=4)
        gen_word()


mode_list = ['Password', 'Passphrase']
mode_str = tk.StringVar(root, value='Password')
mode_drop = tk.OptionMenu(root, mode_str, *mode_list, command=switch_mode)
mode_drop.grid(column=0, row=3)

# Password Frame
pw_frame = tk.Frame(root)
pw_frame.grid(column=0, row=4)


def length_f(v):
    S.length = int(v)


length_label = tk.Label(pw_frame, text='Length')
length_label.grid(column=0, row=0)
length_scale = tk.Scale(pw_frame, from_=4, to=32, orient=tk.HORIZONTAL, command=length_f)
length_scale.set(S.length)
length_scale.grid(column=1, row=0)


class Checkbox:
    def __init__(self, lt, g, sub, add):
        self.lt = lt  # Label Text
        self.g = g  # Grid Row
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


def words_f():
    S.words = int(words_var.get())


words_label = tk.Label(pp_frame, text='Number of Words')
words_label.grid(column=0, row=0)
words_var = tk.IntVar(value=S.words)
words_spinbox = tk.Spinbox(pp_frame, from_=1, to=16, width=2, state='readonly', textvariable=words_var, command=words_f)
words_spinbox.grid(column=1, row=0)


def callback(v):
    if len(v) <= 1:
        S.sep = v
        return True
    else:
        return False


reg = root.register(callback)

sep_label = tk.Label(pp_frame, text='Separator')
sep_label.grid(column=0, row=1)
sep_var = tk.StringVar(value=S.sep)
sep_entry = tk.Entry(pp_frame, width=2, validate="key", validatecommand=(reg, '%P'))
sep_entry.grid(column=1, row=1)
sep_entry.insert(0, S.sep)


def minlength_f():
    if int(minlength_var.get()) > S.maxlength:  # When minlength is greater than maxlength
        S.minlength = S.maxlength
    else:
        S.minlength = int(minlength_var.get())
    minlength_spinbox.config(to=S.maxlength)


minlength_label = tk.Label(pp_frame, text='Min Length')
minlength_label.grid(column=0, row=2)
minlength_var = tk.IntVar(value=S.minlength)
minlength_spinbox = tk.Spinbox(pp_frame, from_=1, to=16, width=2, state='readonly', textvariable=minlength_var, command=minlength_f)
minlength_spinbox.grid(column=1, row=2)


def maxlength_f():
    if int(maxlength_var.get()) < S.minlength:  # When maxlength is less than minlength
        S.maxlength = S.minlength
    else:
        S.maxlength = int(maxlength_var.get())
    maxlength_spinbox.config(from_=S.minlength)


maxlength_label = tk.Label(pp_frame, text='Max Length')
maxlength_label.grid(column=0, row=3)
maxlength_var = tk.IntVar(value=S.maxlength)
maxlength_spinbox = tk.Spinbox(pp_frame, from_=1, to=16, width=2, state='readonly', textvariable=maxlength_var, command=maxlength_f)
maxlength_spinbox.grid(column=1, row=3)


def casing_f(c):
    if c == 'Lowercase':
        S.casing = 'lower'
    elif c == 'Uppercase':
        S.casing = 'upper'
    elif c == 'Titlecase':
        S.casing = 'title'
    print(S.casing)


casing_label = tk.Label(pp_frame, text='Casing')
casing_label.grid(column=0, row=4)
casing_list = ['Lowercase', 'Uppercase', 'Titlecase']
casing_str = tk.StringVar(value='Lowercase')
casing_drop = tk.OptionMenu(pp_frame, casing_str, *casing_list, command=casing_f)
casing_drop.grid(column=1, row=4)


def number_f():
    if number_var.get() == 0:
        S.number = False
    elif number_var.get() == 1:
        S.number = True


number_label = tk.Label(pp_frame, text='Number').grid(column=0, row=5)
number_var = tk.IntVar(pp_frame)
number_check = tk.Checkbutton(pp_frame, variable=number_var, command=number_f)
number_check.grid(column=1, row=5)
number_check.invoke()


# Generate Button
def generate():
    if mode_str.get() == 'Password':
        gen_word()
    elif mode_str.get() == 'Passphrase':
        gen_phrase()


generate_button = tk.Button(root, text="Regenerate Password", command=generate)
generate_button.grid(column=0, row=1)
generate_button.invoke()

root.mainloop()
