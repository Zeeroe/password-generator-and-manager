import tkinter as tk
from generatorPanel import *


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('1Pass')
        self.root.geometry('300x400')

        self.generatorFrame = tk.Frame(self.root).grid()
        self.generatorPanel = generatorPanel(self.generatorFrame)

    def start(self):
        self.root.mainloop()
