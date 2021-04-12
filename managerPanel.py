import tkinter as tk


class managerPanel:
    def __init__(self, root):
        self.frame = tk.Frame(root)

        self.listbox_var = []
        self.listbox = tk.Listbox(self.frame, height=22, width=40, listvariable=self.listbox_var)
        self.listbox.grid()

    def insert_listbox(self, new):
        self.listbox.insert(tk.END, new)
