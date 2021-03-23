import tkinter as tk
from pwPanel import *
from ppPanel import *
from settings import S
import random_word
import random

rw = random_word.RandomWords()


class mainPanel:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.frame.grid()

        self.text_entry = tk.Entry(self.frame, width=50, justify=tk.CENTER)
        self.text_entry.grid(column=0, row=0)

        self.mode_list = ['Password', 'Passphrase']
        self.mode_str = tk.StringVar(self.frame, value='Password')
        self.mode_drop = tk.OptionMenu(self.frame, self.mode_str, *self.mode_list, command=self.switch_mode)
        self.mode_drop.grid(column=0, row=3)

        self.generate_button = tk.Button(self.frame, text="Regenerate Password", command=self.generate)
        self.generate_button.grid(column=0, row=1)

        self.settings_label = tk.Label(self.frame, text='Settings')
        self.settings_label.grid(column=0, row=2)

        self.pwFrame = tk.Frame(self.frame)
        self.pwFrame.grid(column=0, row=4)
        self.pwPanel = pwPanel(self.pwFrame, S)

        self.ppFrame = tk.Frame(self.frame)
        self.ppPanel = ppPanel(self.ppFrame, S)

    def switch_mode(self, mode):
        if mode == 'Passphrase':
            self.pwFrame.grid_forget()
            self.ppFrame.grid(column=0, row=4)
            self.gen_phrase()
        elif mode == 'Password':
            self.ppFrame.grid_forget()
            self.pwFrame.grid(column=0, row=4)
            self.gen_word()

    def generate(self):
        if self.mode_str.get() == 'Password':
            self.gen_word()
        elif self.mode_str.get() == 'Passphrase':
            self.gen_phrase()

    def gen_word(self):
        try:
            password = ''.join(random.choice(S.characters) for _ in range(S.length))
        except IndexError:
            password = ''
        self.text_entry.delete(0, len(self.text_entry.get()))
        self.text_entry.insert(1, password)

    def gen_phrase(self):
        try:
            sep = S.sep
            list_ = rw.get_random_words(
                limit=S.words,
                minLength=S.minlength,
                maxLength=S.maxlength)

            if S.number:
                index_ = random.randint(0, len(list_) - 1)
                number_ = str(random.randint(0, 9))
                list_[index_] += number_

            passphrase = sep.join(list_)

            if S.casing == 'lower':
                passphrase = passphrase.lower()
            elif S.casing == 'upper':
                passphrase = passphrase.upper()
            elif S.casing == 'title':
                passphrase = passphrase.title()

            self.text_entry.delete(0, len(self.text_entry.get()))
            self.text_entry.insert(0, passphrase)

        except TypeError:
            print('TypeError')
            self.gen_phrase()
