import tkinter as tk
import random_word
import re

rw = random_word.RandomWords()


class Checkbox:
    def __init__(self, so, parent, g, sub, add):
        self.so = so  # Settings Object
        self.sub = sub  # Characters to remove (Regex)
        self.add = add  # Characters to add

        text = sub[1:-1]

        self.label = tk.Label(parent, text=text).grid(column=0, row=g)
        self.var = tk.IntVar(parent)
        self.check = tk.Checkbutton(parent, variable=self.var, command=self.func)
        self.check.grid(column=1, row=g)
        self.check.invoke()

    def func(self):
        if self.var.get() == 0:
            self.so.characters = re.sub(self.sub, '', self.so.characters)
        elif self.var.get() == 1:
            self.so.characters += self.add


class pwPanel:
    def __init__(self, frame, settings):
        self.frame = frame
        self.S = settings

        self.length_label = tk.Label(self.frame, text='Length')
        self.length_label.grid(column=0, row=0)
        self.length_scale = tk.Scale(self.frame, from_=4, to=32, orient=tk.HORIZONTAL, command=self.length_f)
        self.length_scale.set(self.S.length)
        self.length_scale.grid(column=1, row=0)

        self.low = Checkbox(self.S, self.frame, 1, '[a-z]', 'abcdefghijklmnopqrstuvwxyz')
        self.up = Checkbox(self.S, self.frame, 2, '[A-Z]', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.num = Checkbox(self.S, self.frame, 3, '[0-9]', '0123456789')
        self.sym = Checkbox(self.S, self.frame, 4, '[!@#$%^&*]', '!@#$%^&*')

    def length_f(self, v):
        self.S.length = int(v)
