import tkinter as tk
import random_word
import random

rw = random_word.RandomWords()


class Checkbox:
    def __init__(self, panel, g, txt, ch):
        self.panel = panel  # pwPanel
        self.frame = self.panel.frame  # pwFrame
        self.S = self.panel.S  # Settings Object
        self.ch = ch

        self.label = tk.Label(self.frame, text=txt)
        self.label.grid(column=0, row=g)

        self.var = tk.IntVar(self.panel.frame)
        self.check = tk.Checkbutton(self.frame, variable=self.var, command=self.func)
        self.check.select()
        self.check.grid(column=1, row=g)

    def func(self):
        if self.var.get() == 0:
            if self.panel.last_box():
                self.S.characters[self.ch + '-'] = self.S.characters.pop(self.ch)
            else:
                self.check.select()

        elif self.var.get() == 1:
            self.S.characters[self.ch] = self.S.characters.pop(self.ch + '-')


class pwPanel:
    def __init__(self, frame, settings):
        self.frame = frame
        self.S = settings

        self.length_label = tk.Label(self.frame, text='Length')
        self.length_label.grid(column=0, row=0)
        self.length_scale = tk.Scale(self.frame, from_=4, to=32, orient=tk.HORIZONTAL, command=self.length_f)
        self.length_scale.set(self.S.length)
        self.length_scale.grid(column=1, row=0)

        self.low = Checkbox(self, 1, 'a-z', 'a')
        self.upp = Checkbox(self, 2, 'A-Z', 'A')
        self.num = Checkbox(self, 3, '0-9', '1')
        self.sym = Checkbox(self, 4, '!@#$%^&*', '!')

    def last_box(self):
        if self.low.var.get() == 0 and \
           self.upp.var.get() == 0 and \
           self.num.var.get() == 0 and \
           self.sym.var.get() == 0:
            return False
        else:
            return True

    def gen_word(self, te):
        try:
            pool = ''
            for key in self.S.characters.keys():
                if '-' not in key:
                    pool += (self.S.characters[key])

            password = ''.join(random.choice(pool) for _ in range(self.S.length))

            # Ensuring the string has at least 1 character from each category
            for key in self.S.characters.keys():
                if '-' not in key:
                    check = False
                    for character in self.S.characters[key]:
                        if character in password:
                            check = True
                            break
                    if not check:
                        password = password[1:-1] \
                                   + random.choice(self.S.characters[key]) \
                                   + password[0]

            _ = random.sample(list(password), k=len(password))
            password = ''.join(_)

        except IndexError:
            print('IndexError')
            password = ''

        te.delete(0, len(te.get()))
        te.insert(1, password)

    def length_f(self, v):
        self.S.length = int(v)
