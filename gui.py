import tkinter as tk
from settings import Settings
import random, string, random_word

S = Settings()
rw = random_word.RandomWords()


def gen_word():
    password = ''.join(random.choice(S.characters) for _ in range(S.length))
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

# Passphrase Frame
pp_frame = tk.Frame(root)
pp_frame.grid(column=0, row=4)


def switch_mode(v):
    print(v)


# Dropdown Menu
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
