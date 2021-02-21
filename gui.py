from tkinter import *
from settings import Settings
import random, string, random_word

S = Settings()
rw = random_word.RandomWords()

# Window
window = Tk()
window.title("1Pass")
window.geometry('400x200')

# Text
entry_pw = Entry(window, width=32)
entry_pw.grid(column=1, row=0)
entry_pw.focus()

entry_pp = Entry(window, width=32)
entry_pp.grid(column=1, row=1)
entry_pp.focus()

# Label
lbl_pw = Label(window, width=12, text="Password:")
lbl_pw.grid(column=0, row=0)

lbl_pp = Label(window, width=12, text="Passphrase:")
lbl_pp.grid(column=0, row=1)


def generate_password():
    password = ''.join(random.choice(S.characters) for _ in range(S.length))
    entry_pw.delete(0, len(entry_pw.get()))
    entry_pw.insert(1, password)


def generate_passphrase():
    try:
        passphrase = S.separator.join(rw.get_random_words(limit=S.limit,
                                                          minLength=S.minlength,
                                                          maxLength=S.maxlength,
                                                          hasDictionaryDef='True'))

        passphrase = passphrase.lower()
        entry_pp.delete(0, len(entry_pp.get()))
        entry_pp.insert(1, passphrase)

    except TypeError:
        print('TypeError')
        generate_passphrase()


btn = Button(window, text="Generate Password", command=generate_password)
btn.grid(column=2, row=0)
btn2 = Button(window, text="Generate Passphrase", command=generate_passphrase)
btn2.grid(column=2, row=1)

window.mainloop()
