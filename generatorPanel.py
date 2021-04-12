import tkinter as tk
from pwPanel import *
from ppPanel import *
from syPanel import *
from settings import S


class generatorPanel:
    def __init__(self, root, mp):
        self.mp = mp
        self.frame = tk.Frame(root)
        self.frame.grid(column=0, row=1)

        self.text_entry = tk.Entry(self.frame, width=50, justify=tk.CENTER)
        self.text_entry.grid(column=0, row=0)

        self.generate_button = tk.Button(self.frame, text="Regenerate Password", command=self.generate)
        self.generate_button.grid(column=0, row=1)

        self.settings_label = tk.Label(self.frame, text='Settings')
        self.settings_label.grid(column=0, row=2)

        self.modeFrame = tk.Frame(self.frame)
        self.modeFrame.grid(column=0, row=3)
        self.minlength_label = tk.Label(self.modeFrame, text='Mode    ')
        self.minlength_label.grid(column=0, row=0)
        self.mode_list = ['Password', 'Passphrase', 'Synonym']
        self.mode = 'Password'
        self.mode_str = tk.StringVar(self.modeFrame, value=self.mode)
        self.mode_drop = tk.OptionMenu(self.modeFrame, self.mode_str, *self.mode_list, command=self.switch_mode)
        self.mode_drop.grid(column=1, row=0)

        self.pwFrame = tk.Frame(self.frame)
        self.pwPanel = pwPanel(self.pwFrame, S)

        self.ppFrame = tk.Frame(self.frame)
        self.ppPanel = ppPanel(self.ppFrame, S)

        self.syFrame = tk.Frame(self.frame)
        self.syPanel = syPanel(self.syFrame, S)

        self.switch_mode(self.mode)

    def switch_mode(self, mode):
        if mode == 'Password':
            self.ppFrame.grid_forget()
            self.syFrame.grid_forget()
            self.pwFrame.grid(column=0, row=4)
        elif mode == 'Passphrase':
            self.pwFrame.grid_forget()
            self.syFrame.grid_forget()
            self.ppFrame.grid(column=0, row=4)
        elif mode == 'Synonym':
            self.pwFrame.grid_forget()
            self.ppFrame.grid_forget()
            self.syFrame.grid(column=0, row=4)

    def generate(self):
        if self.mode_str.get() == 'Password':
            self.pwPanel.gen_word(self.text_entry)
        elif self.mode_str.get() == 'Passphrase':
            self.ppPanel.gen_phrase(self.text_entry)
        elif self.mode_str.get() == 'Synonym':
            self.syPanel.gen_phrase(self.text_entry)
        self.mp.insert_listbox(self.text_entry.get())
