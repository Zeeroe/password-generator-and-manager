import os
import tkinter as tk
from PwPanel import *
from PpPanel import *
from RwPanel import *
from settings import S


class GeneratorFrame:
    def __init__(self, parent, images):
        self.frame = tk.Frame(parent)
        self.images = images

        self.topFrame = tk.Frame(self.frame)
        self.topFrame.grid(column=0, row=0)

        self.text_entry = tk.Entry(self.topFrame, width=40, justify=tk.CENTER)
        self.text_entry.grid(column=0, row=0)

        self.history_listbox = tk.Listbox(self.topFrame, height=22, width=40)
        self.history_button = tk.Button(self.topFrame, image=self.images['history'], height=20, width=20, command=self.history)
        self.history_button.grid(column=1, row=0, sticky='NE')

        self.generate_button = tk.Button(self.frame, text="Regenerate Password", command=self.generate)
        self.generate_button.grid(column=0, row=1)

        self.modeFrame = tk.Frame(self.frame)
        self.modeFrame.grid(column=0, row=3)
        self.mode_label = tk.Label(self.modeFrame, text='Mode    ')
        self.mode_label.grid(column=0, row=0)
        self.mode_list = ['Password', 'Passphrase', 'Related words']
        self.mode = 'Password'
        self.mode_str = tk.StringVar(self.modeFrame, value=self.mode)
        self.mode_drop = tk.OptionMenu(self.modeFrame, self.mode_str, *self.mode_list, command=self.switch_mode)
        self.mode_drop.grid(column=1, row=0)

        self.PwFrame = tk.Frame(self.frame)
        self.PwPanel = PwPanel(self.PwFrame, S)

        self.PpFrame = tk.Frame(self.frame)
        self.PpPanel = PpPanel(self.PpFrame, S)

        self.RwFrame = tk.Frame(self.frame)
        self.RwPanel = RwPanel(self.RwFrame, S)

        self.switch_mode(self.mode)

    def history(self):
        if self.text_entry.winfo_ismapped():
            self.text_entry.grid_forget()
            self.history_listbox.grid(column=0, row=0)
        elif self.history_listbox.winfo_ismapped():
            self.history_listbox.grid_forget()
            self.text_entry.grid(column=0, row=0)

    def insert_history(self, new):
        self.history_listbox.insert(0, new)

    def switch_mode(self, mode):
        if mode == 'Password':
            self.PpFrame.grid_forget()
            self.RwFrame.grid_forget()
            self.PwFrame.grid(column=0, row=4)
        elif mode == 'Passphrase':
            self.PwFrame.grid_forget()
            self.RwFrame.grid_forget()
            self.PpFrame.grid(column=0, row=4)
            self.PpPanel.recheck_settings()
        elif mode == 'Related words':
            self.PwFrame.grid_forget()
            self.PpFrame.grid_forget()
            self.RwFrame.grid(column=0, row=4)
            self.RwPanel.recheck_settings()

    def generate(self):
        if   self.mode_str.get() == 'Password':      self.PwPanel.gen_word(self.text_entry)
        elif self.mode_str.get() == 'Passphrase':    self.PpPanel.gen_phrase(self.text_entry)
        elif self.mode_str.get() == 'Related words': self.RwPanel.gen_phrase(self.text_entry)
        self.insert_history(self.text_entry.get())
