import tkinter as tk
from dockPanel import *
from generatorPanel import *
from managerPanel import *


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('1Pass')
        self.root.geometry('300x400')
        self.frame = tk.Frame(self.root).grid()

        self.managerPanel = managerPanel(self.frame)

        self.generatorPanel = generatorPanel(self.frame, self.managerPanel)

        self.dockPanel = dockPanel(self.frame, self.generatorPanel, self.managerPanel)

    def start(self):
        self.root.mainloop()
