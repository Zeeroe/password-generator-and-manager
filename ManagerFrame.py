import tkinter as tk
import csv


class Login:
    def __init__(self, login_list, row, site='Website', user='Username', pw='Password'):
        self.frame = tk.Frame(login_list, bd=1, relief=tk.RIDGE)
        self.frame.grid(column=0, row=row)

        self.site = site
        self.user = user
        self.pw = pw

        self.label_frame = tk.Frame(self.frame)
        self.label_frame.grid(column=0, row=0)

        self.site_label = tk.Label(self.label_frame, width=28, height=1, text=self.site)
        self.site_label.grid(column=0, row=0)

        self.user_label = tk.Label(self.label_frame, width=28, height=1, text=self.user)
        self.user_label.grid(column=0, row=1)

        self.edit_button = tk.Button(self.frame, text='E', width=2, command=self.edit)
        self.edit_button.grid(column=1, row=0)

        self.copy_button = tk.Button(self.frame, text='C', width=2, command=self.copy)
        self.copy_button.grid(column=2, row=0)

        self.delete_button = tk.Button(self.frame, text='D', width=2, command=self.delete)
        self.delete_button.grid(column=3, row=0)

    def edit(self):
        print('E ' + self.site + ' ' + self.user)

    def copy(self):
        print('C ' + self.site + ' ' + self.user)

    def delete(self):
        print('D ' + self.site + ' ' + self.user)


class ManagerFrame:
    def __init__(self, root):
        self.frame = tk.Frame(root)

        self.list_logins = []

        self.top_frame = tk.Frame(self.frame)
        self.top_frame.grid(row=0)
        self.bottom_frame = tk.Frame(self.frame)
        self.bottom_frame.grid(column=0, row=1)

        self.add_button = tk.Button(self.top_frame, width=10, text='Add Login', command=self.add_login)
        self.add_button.grid(column=0, row=0)

        self.search = tk.Entry(self.top_frame, width=50)
        self.search.grid(column=0, row=1)

        self.canvas = tk.Canvas(self.bottom_frame, width=275, height=310)
        self.canvas.grid(column=0, row=0)
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)

        self.logins_frame = tk.Frame(self.canvas, width=300, height=300)

        self.scrollbar = tk.Scrollbar(self.bottom_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(column=1, row=0, sticky='ns')

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.logins_frame, anchor='nw')

        with open('logins.txt', 'r') as logins_file:
            logins = csv.reader(logins_file, delimiter=',')
            h = 0
            row = 0
            for login in logins:
                self.list_logins.append(Login(self.logins_frame, row, login[0], login[1], login[2]))
                row += 1
                h += 44
                self.logins_frame.configure(height=h)

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_login(self):
        pass

    def _on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
