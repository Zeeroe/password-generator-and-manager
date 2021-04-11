import tkinter as tk
from random_word import RandomWords
import random
import re

rw = RandomWords()


class syPanel:
    def __init__(self, frame, settings):
        self.frame = frame
        self.S = settings

        self.words_label = tk.Label(self.frame, text='Number of Words')
        self.words_label.grid(column=0, row=0)
        self.words_var = tk.IntVar(value=self.S.words)
        self.words_spinbox = tk.Spinbox(self.frame, from_=1, to=16, width=2, state='readonly',
                                        textvariable=self.words_var, command=self.words_f)
        self.words_spinbox.grid(column=1, row=0)

        self.minlength_label = tk.Label(self.frame, text='Min Length')
        self.minlength_label.grid(column=0, row=1)
        self.minlength_var = tk.IntVar(value=self.S.minlength)
        self.minlength_spinbox = tk.Spinbox(self.frame, from_=2, to=16, width=2, state='readonly',
                                            textvariable=self.minlength_var, command=self.minlength_f)
        self.minlength_spinbox.grid(column=1, row=1)

        self.maxlength_label = tk.Label(self.frame, text='Max Length')
        self.maxlength_label.grid(column=0, row=2)
        self.maxlength_var = tk.IntVar(value=self.S.maxlength)
        self.maxlength_spinbox = tk.Spinbox(self.frame, from_=2, to=16, width=2, state='readonly',
                                            textvariable=self.maxlength_var, command=self.maxlength_f)
        self.maxlength_spinbox.grid(column=1, row=2)

        self.casing_label = tk.Label(self.frame, text='Casing')
        self.casing_label.grid(column=0, row=4)
        self.casing_list = ['Lowercase', 'Uppercase', 'Titlecase']
        self.casing_str = tk.StringVar(value=self.S.casing)
        self.casing_drop = tk.OptionMenu(self.frame, self.casing_str, *self.casing_list, command=self.casing_f)
        self.casing_drop.grid(column=1, row=4)

        self.reg = self.frame.register(self.separator_f)

        self.sep_label = tk.Label(self.frame, text='Separator')
        self.sep_label.grid(column=0, row=3)
        self.sep_var = tk.StringVar(value=self.S.sep)
        self.sep_entry = tk.Entry(self.frame, width=2, validate="key", validatecommand=(self.reg, '%P'))
        self.sep_entry.grid(column=1, row=3)
        self.sep_entry.insert(0, self.S.sep)

        self.number_label = tk.Label(self.frame, text='Number').grid(column=0, row=5)
        self.number_var = tk.IntVar(self.frame)
        self.number_check = tk.Checkbutton(self.frame, variable=self.number_var, command=self.number_f)
        self.number_check.grid(column=1, row=5)
        self.number_check.invoke()

    def words_f(self):
        self.S.words = int(self.words_var.get())

    def maxlength_f(self):
        if int(self.maxlength_var.get()) < self.S.minlength:  # When maxlength is less than minlength
            self.S.maxlength = self.S.minlength
        else:
            self.S.maxlength = int(self.maxlength_var.get())
        self.maxlength_spinbox.config(from_=self.S.minlength)

    def minlength_f(self):
        if int(self.minlength_var.get()) > self.S.maxlength:  # When minlength is greater than maxlength
            self.S.minlength = self.S.maxlength
        else:
            self.S.minlength = int(self.minlength_var.get())
        self.minlength_spinbox.config(to=self.S.maxlength)

    def casing_f(self, c):
        self.S.casing = c
        print(self.S.casing)

    def separator_f(self, v):
        if len(v) <= 1:
            self.S.sep = v
            return True
        else:
            return False

    def number_f(self):
        if self.number_var.get() == 0:
            self.S.number = False
        elif self.number_var.get() == 1:
            self.S.number = True

    def gen_phrase(self, text_entry):
        try:
            S = self.S
            list_ = rw.get_random_words(limit=S.words, minLength=S.minlength, maxLength=S.maxlength)

            for word in list_:
                x = word
                while not re.search(re.compile('^[aA-zZ]+$'), x):
                    print(x + ' -> ', end='')
                    x = rw.get_random_word(minLength=S.minlength, maxLength=S.maxlength)
                    print(x)
                list_[list_.index(word)] = x

            if S.number:
                index_ = random.randint(0, len(list_) - 1)
                number_ = str(random.randint(0, 9))
                list_[index_] += number_

            passphrase = S.sep.join(list_)

            if S.casing == 'Lowercase':
                passphrase = passphrase.lower()
            elif S.casing == 'Uppercase':
                passphrase = passphrase.upper()
            elif S.casing == 'Titlecase':
                passphrase = passphrase.title()

            text_entry.delete(0, len(text_entry.get()))
            text_entry.insert(0, passphrase)

        except TypeError:  # When get_random_words doesn't return anything, because of rate limit
            self.gen_phrase(text_entry)
