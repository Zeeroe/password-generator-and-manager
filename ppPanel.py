import tkinter as tk


class ppPanel:
    def __init__(self, frame, settings):
        self.frame = frame
        self.S = settings

        self.words_label = tk.Label(self.frame, text='Number of Words')
        self.words_label.grid(column=0, row=0)
        self.words_var = tk.IntVar(value=self.S.words)
        self.words_spinbox = tk.Spinbox(self.frame, from_=1, to=16, width=2, state='readonly',
                                        textvariable=self.words_var,
                                        command=self.words_f)
        self.words_spinbox.grid(column=1, row=0)

        self.reg = self.frame.register(self.callback)

        self.sep_label = tk.Label(self.frame, text='Separator')
        self.sep_label.grid(column=0, row=1)
        self.sep_var = tk.StringVar(value=self.S.sep)
        self.sep_entry = tk.Entry(self.frame, width=2, validate="key", validatecommand=(self.reg, '%P'))
        self.sep_entry.grid(column=1, row=1)
        self.sep_entry.insert(0, self.S.sep)

        self.minlength_label = tk.Label(self.frame, text='Min Length')
        self.minlength_label.grid(column=0, row=2)
        self.minlength_var = tk.IntVar(value=self.S.minlength)
        self.minlength_spinbox = tk.Spinbox(self.frame, from_=1, to=16, width=2, state='readonly',
                                            textvariable=self.minlength_var,
                                            command=self.minlength_f)
        self.minlength_spinbox.grid(column=1, row=2)

        self.maxlength_label = tk.Label(self.frame, text='Max Length')
        self.maxlength_label.grid(column=0, row=3)
        self.maxlength_var = tk.IntVar(value=self.S.maxlength)
        self.maxlength_spinbox = tk.Spinbox(self.frame, from_=1, to=16, width=2, state='readonly',
                                            textvariable=self.maxlength_var,
                                            command=self.maxlength_f)
        self.maxlength_spinbox.grid(column=1, row=3)

        self.casing_label = tk.Label(self.frame, text='Casing')
        self.casing_label.grid(column=0, row=4)
        self.casing_list = ['Lowercase', 'Uppercase', 'Titlecase']
        self.casing_str = tk.StringVar(value='Lowercase')
        self.casing_drop = tk.OptionMenu(self.frame, self.casing_str, *self.casing_list, command=self.casing_f)
        self.casing_drop.grid(column=1, row=4)

        self.number_label = tk.Label(self.frame, text='Number').grid(column=0, row=5)
        self.number_var = tk.IntVar(self.frame)
        self.number_check = tk.Checkbutton(self.frame, variable=self.number_var, command=self.number_f)
        self.number_check.grid(column=1, row=5)
        self.number_check.invoke()

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

    def callback(self, v):
        if len(v) <= 1:
            self.S.sep = v
            return True
        else:
            return False

    def casing_f(self, c):
        if c == 'Lowercase':
            self.S.casing = 'lower'
        elif c == 'Uppercase':
            self.S.casing = 'upper'
        elif c == 'Titlecase':
            self.S.casing = 'title'
        print(self.S.casing)

    def number_f(self):
        if self.number_var.get() == 0:
            self.S.number = False
        elif self.number_var.get() == 1:
            self.S.number = True

    def words_f(self):
        self.S.words = int(self.words_var.get())
