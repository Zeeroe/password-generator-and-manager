import tkinter as tk
import csv


class LoginObj:
    def __init__(self, mger, row, website, user, pw):
        self.frame = tk.Frame(mger.logins_frame, bd=1, relief=tk.RIDGE)
        self.frame.grid(column=0, row=row)

        self.logins_frame = mger.logins_frame
        self.canvas = mger.canvas
        self.root = mger.root
        self.list_logins = mger.list_logins

        self.website = website
        self.user = user
        self.pw = pw

        self.edit_mode = False

        self.entry_frame = tk.Frame(self.frame)
        self.entry_frame.grid(column=0, row=0)

        self.site_entry = tk.Entry(self.entry_frame, width=33, justify=tk.CENTER)
        self.site_entry.insert(0, self.website)
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
        h = self.logins_frame.winfo_height()
        if not self.edit_mode:
            for field in self.list_fields:
                field.configure(state=tk.NORMAL)
            self.pw_entry.grid()
            self.logins_frame.configure(height=(h+20))
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            self.edit_mode = True
        else:
            new = []  # temp list to store (possibly updated) website, user, password from fields
            for field in self.list_fields:
                field.configure(state=tk.DISABLED)
                new.append(field.get())
            index = self.list_logins.index([self.website, self.user, self.pw])
            self.list_logins[index] = new  # update login information
            [self.website, self.user, self.pw] = new
            self.update_file()

            self.pw_entry.grid_forget()
            self.logins_frame.configure(height=(h-20))
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            self.edit_mode = False

    def copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.pw_entry.get())

    def delete(self):
        self.frame.grid_forget()
        self.list_logins.remove([self.website, self.user, self.pw])
        self.update_file()
        h = self.logins_frame.winfo_height()
        self.logins_frame.configure(height=(h - 40))
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def update_file(self):
        logins_file = open('logins.txt', 'w', newline='')
        writer = csv.writer(logins_file, delimiter=',')
        writer.writerows(self.list_logins)
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

        self.logins_file = open('logins.txt', 'r')
        self.list_logins = list(csv.reader(self.logins_file, delimiter=','))
        self.import_logins()

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_login(self):
        row = len(self.list_logins_obj) + 1
        self.list_logins_obj.append(LoginObj(self, row, '', '', ''))
        self.list_logins.append(['', '', ''])
        h = self.logins_frame.winfo_height()
        self.logins_frame.configure(height=(h + 40))
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.yview_moveto(1)

    def _on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    def import_logins(self):
        h = 0
        row = 0
        for login in self.list_logins:
            self.list_logins_obj.append(LoginObj(self, row, login[0], login[1], login[2]))
            row += 1
            h += 40
            self.logins_frame.configure(height=h)
        self.logins_file.close()
