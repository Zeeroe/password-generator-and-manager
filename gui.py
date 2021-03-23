import tkinter as tk
from mainPanel import *


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('1Pass')
        self.root.geometry('300x400')

        self.mainframe = tk.Frame(self.root)
        self.mainframe.grid()

        self.mainPanel = mainPanel(self.mainframe)
        self.mainPanel.generate_button.invoke()

    def start(self):
        self.root.mainloop()
