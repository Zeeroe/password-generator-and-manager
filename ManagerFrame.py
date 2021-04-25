import tkinter as tk
import csv


class LoginObj:
    def __init__(self, login_list, root, row, site, user, pw):
        self.frame = tk.Frame(login_list, bd=1, relief=tk.RIDGE)
        self.frame.grid(column=0, row=row)
        self.root = root

        self.site = site
        self.user = user
        self.pw = pw

        self.edit_mode = False

        self.entry_frame = tk.Frame(self.frame)
        self.entry_frame.grid(column=0, row=0)

        self.site_entry = tk.Entry(self.entry_frame, width=33)
        self.site_entry.insert(0, self.site)
        self.site_entry.grid(column=0, row=0)

        self.user_entry = tk.Entry(self.entry_frame, width=33)
        self.user_entry.insert(0, self.user)
        self.user_entry.grid(column=0, row=1)

        self.pw_entry = tk.Entry(self.entry_frame, width=33)
        self.pw_entry.insert(0, self.pw)

        self.list_fields = [self.site_entry, self.user_entry, self.pw_entry]

        for field in self.list_fields:
            field.configure(state=tk.DISABLED)

        self.edit_button = tk.Button(self.frame, text='E', width=2, command=self.edit)
        self.edit_button.grid(column=1, row=0, sticky='n')

        self.copy_button = tk.Button(self.frame, text='C', width=2, command=self.copy)
        self.copy_button.grid(column=2, row=0, sticky='n')

        self.delete_button = tk.Button(self.frame, text='D', width=2, command=self.delete)
        self.delete_button.grid(column=3, row=0, sticky='n')

    def edit(self):
        if not self.edit_mode:
            for field in self.list_fields:
                field.configure(state=tk.NORMAL)
            self.pw_entry.grid(column=0, row=2)
            self.edit_mode = True
        else:
            for field in self.list_fields:
                field.configure(state=tk.DISABLED)
            self.pw_entry.grid_forget()
            self.edit_mode = False

    def copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.pw_entry.get())

    def delete(self):
        self.frame.grid_forget()
        logins_file = open('logins.txt', 'r')
        list_logins = list(csv.reader(logins_file, delimiter=','))
        list_logins.remove([self.site, self.user, self.pw])
        logins_file.close()

        logins_file = open('logins.txt', 'w', newline='')
        x = csv.writer(logins_file, delimiter=',')
        x.writerows(list_logins)
        logins_file.close()


class ManagerFrame:
    def __init__(self, frame, root):
        self.frame = tk.Frame(frame)
        self.root = root

        self.list_logins_obj = []

        self.top_frame = tk.Frame(self.frame)
        self.top_frame.grid(row=0)
        self.bottom_frame = tk.Frame(self.frame)
        self.bottom_frame.grid(column=0, row=1)

        self.add_button = tk.Button(self.top_frame, width=10, text='Add Login', command=self.add_login)
        self.add_button.grid(column=0, row=0, sticky='w')

        self.search = tk.Entry(self.top_frame, width=49)
        self.search.grid(column=0, row=1, sticky='w')

        self.canvas = tk.Canvas(self.bottom_frame, width=275, height=310, relief=tk.FLAT)
        self.canvas.grid(column=0, row=0)
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)

        self.logins_frame = tk.Frame(self.canvas, width=300, height=300)

        self.scrollbar = tk.Scrollbar(self.bottom_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(column=1, row=0, sticky='ns')

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.logins_frame, anchor='nw')

        self.import_logins()

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_login(self):
        pass

    def _on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    def import_logins(self):
        logins_file = open('logins.txt', 'r')
        list_logins = list(csv.reader(logins_file, delimiter=','))
        h = 0
        row = 0
        for login in list_logins:
            self.list_logins_obj.append(LoginObj(self.logins_frame, self.root, row, login[0], login[1], login[2]))
            row += 1
            h += 44
            self.logins_frame.configure(height=h)
        logins_file.close()
