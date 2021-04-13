import tkinter as tk
from DockFrame import *
from GeneratorFrame import *
from ManagerFrame import *


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('1Pass')
        self.root.geometry('300x400')
        self.frame = tk.Frame(self.root).grid()

        self.ManagerFrame = ManagerFrame(self.frame)

        self.GeneratorFrame = GeneratorFrame(self.frame)

        self.DockFrame = DockFrame(self.frame, self.GeneratorFrame, self.ManagerFrame)

    def start(self):
        self.root.mainloop()
