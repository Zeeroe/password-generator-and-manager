import tkinter as tk
from pwPanel import *
from ppPanel import *
from syPanel import *
from settings import S


class generatorPanel:
    def __init__(self, root):
        self.frame = tk.Frame(root)
        self.frame.grid(column=0, row=1)

        self.text_entry = tk.Entry(self.frame, width=50, justify=tk.CENTER)
        self.text_entry.grid(column=0, row=0)

        self.generate_button = tk.Button(self.frame, text="Regenerate Password", command=self.generate)
        self.generate_button.grid(column=0, row=1)

        self.settings_label = tk.Label(self.frame, text='Settings')
        self.settings_label.grid(column=0, row=2)

        self.mode_list = ['Password', 'Passphrase', 'Synonym']
        self.mode = 'Password'
        self.mode_str = tk.StringVar(self.frame, value=self.mode)
        self.mode_drop = tk.OptionMenu(self.frame, self.mode_str, *self.mode_list, command=self.switch_mode)
        self.mode_drop.grid(column=0, row=3)

        self.pwFrame = tk.Frame(self.frame)
        self.pwPanel = pwPanel(self.pwFrame, S)

        self.ppFrame = tk.Frame(self.frame)
        self.ppPanel = ppPanel(self.ppFrame, S)

        self.syFrame = tk.Frame(self.frame)
        self.syPanel = syPanel(self.syFrame, S)

        self.switch_mode(self.mode)
        self.generate_button.invoke()

    def switch_mode(self, mode):
        if mode == 'Password':
            self.ppFrame.grid_forget()
            self.syFrame.grid_forget()
            self.pwFrame.grid(column=0, row=4)
            self.pwPanel.gen_word(self.text_entry)
        elif mode == 'Passphrase':
            self.pwFrame.grid_forget()
            self.syFrame.grid_forget()
            self.ppFrame.grid(column=0, row=4)
            self.ppPanel.gen_phrase(self.text_entry)
        elif mode == 'Synonym':
            self.pwFrame.grid_forget()
            self.ppFrame.grid_forget()
            self.syFrame.grid(column=0, row=4)
            self.syPanel.gen_phrase(self.text_entry)

    def generate(self):
        if self.mode_str.get() == 'Password':
            self.pwPanel.gen_word(self.text_entry)
        elif self.mode_str.get() == 'Passphrase':
            self.ppPanel.gen_phrase(self.text_entry)
        elif self.mode_str.get() == 'Synonym':
            self.syPanel.gen_phrase(self.text_entry)
