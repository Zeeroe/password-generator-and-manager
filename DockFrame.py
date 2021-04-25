import tkinter as tk


class DockFrame:
    def __init__(self, frame, gf, mf):
        self.frame = tk.Frame(frame)
        self.frame.grid(column=0, row=0)

        self.gf = gf
        self.mf = mf

        self.to_generator_button = tk.Button(self.frame, width=20, height=2, text="Generator", command=self.to_generator_f)
        self.to_generator_button.grid(column=0, row=0)

        self.to_manager_button = tk.Button(self.frame, width=20, height=2, text="Manager", command=self.to_manager_f)
        self.to_manager_button.grid(column=1, row=0)

    def to_generator_f(self):
        self.mf.frame.grid_forget()
        self.gf.frame.grid()

    def to_manager_f(self):
        self.gf.frame.grid_forget()
        self.mf.frame.grid()
