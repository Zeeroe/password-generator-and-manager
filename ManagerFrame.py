import tkinter as tk
import pyAesCrypt
import json
import os

bufferSize = 64 * 1024


class LoginObj:
    def __init__(self, mf, row, website, user, pw):
        self.frame = tk.Frame(mf.logins_frame, bd=1, relief=tk.RIDGE)
        self.frame.grid(column=0, row=row)

        self.mf = mf
        self.logins_frame = mf.logins_frame
        self.canvas = mf.canvas
        self.root = mf.root
        self.data_logins = mf.data_logins

        self.website = website
        self.user = user
        self.pw = pw

        self.edit_bool = False

        self.entry_frame = tk.Frame(self.frame)
        self.entry_frame.grid(column=0, row=0)

        self.site_entry = tk.Entry(self.entry_frame, width=33, justify=tk.CENTER)
        self.site_entry.grid(column=0, row=0)
        self.site_entry.insert(0, self.website)

        self.user_entry = tk.Entry(self.entry_frame, width=33)
        self.user_entry.grid(column=0, row=1)
        self.user_entry.insert(0, self.user)

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

        if not self.edit_bool:
            for field in self.list_fields:
                field.configure(state=tk.NORMAL)
            self.pw_entry.grid()
            self.logins_frame.configure(height=(h+20))
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            self.edit_bool = True
        else:
            new = []  # temp list to store (possibly updated) website, user, password from fields
            for field in self.list_fields:
                new.append(field.get())
                field.configure(state=tk.DISABLED)
            self.pw_entry.grid_forget()
            self.logins_frame.configure(height=(h-20))
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            self.edit_bool = False

            if [self.website, self.user, self.pw] != new:
                index = self.data_logins['logins'].index([self.website, self.user, self.pw])
                self.data_logins['logins'][index] = new  # update login information
                [self.website, self.user, self.pw] = new
                self.mf.encrypt()

    def copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.pw_entry.get())

    def delete(self):
        self.frame.grid_forget()
        h = self.logins_frame.winfo_height()
        self.logins_frame.configure(height=(h - 40))
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.data_logins['logins'].remove([self.website, self.user, self.pw])
        self.mf.encrypt()


class LockFrame:
    def __init__(self, mf):
        self.mf = mf
        self.frame = tk.Frame(mf.frame)

        self.prompt_label = tk.Label(self.frame, text='Enter Keycode')
        self.prompt_label.grid(column=0, row=0)

        self.keycode_entry = tk.Entry(self.frame, width=40)
        self.keycode_entry.grid(column=0, row=1)

        self.unlock_button = tk.Button(self.frame, text='Unlock', command=self.unlock_f)
        self.unlock_button.grid(column=0, row=2)

    def unlock_f(self):
        keycode = self.keycode_entry.get()
        if len(keycode) >= 1:
            self.mf.decrypt(keycode)
            if len(self.mf.data_logins) != 0 and self.mf.data_logins['key'] == keycode:
                self.mf.import_logins()
                self.frame.grid_forget()
                self.mf.manager_frame.grid()


class SetFrame:
    def __init__(self, mf):
        self.mf = mf
        self.frame = tk.Frame(mf.frame)

        self.prompt_label = tk.Label(self.frame, text='Enter Keycode')
        self.prompt_label.grid(column=0, row=0)

        self.keycode_entry = tk.Entry(self.frame, width=40)
        self.keycode_entry.grid(column=0, row=1)

        self.set_key_button = tk.Button(self.frame, text='Set New Keycode', command=self.set_key_f)
        self.set_key_button.grid(column=0, row=2)

    def set_key_f(self):
        keycode = self.keycode_entry.get()
        if len(keycode) >= 1:
            self.mf.set_frame.frame.grid_forget()
            self.mf.manager_frame.grid()

            self.mf.data_logins['key'] = keycode
            self.mf.encrypt()


def is_first_time():
    if os.path.exists("logins.json.aes"): return False
    else: return True


class ManagerFrame:
    def __init__(self, parent, root):
        self.frame = tk.Frame(parent)
        self.root = root

        self.data_logins = {"key": "", "logins": []}

        self.lock_frame = LockFrame(self)
        self.set_frame = SetFrame(self)

        if is_first_time(): self.set_frame.frame.grid()
        else: self.lock_frame.frame.grid()

        self.manager_frame = tk.Frame(self.frame)
        self.top_frame = tk.Frame(self.manager_frame)
        self.top_frame.grid(row=0, sticky='w')
        self.mid_frame = tk.Frame(self.manager_frame)
        #self.mid_frame.grid(row=1, sticky='w')
        self.bottom_frame = tk.Frame(self.manager_frame)
        self.bottom_frame.grid(row=2)

        self.add_button = tk.Button(self.top_frame, text='Add Login', command=self.add_login)
        self.add_button.grid(column=0, row=0)

        self.to_set_button = tk.Button(self.top_frame, text='Set Keycode', command=self.to_set_f)
        self.to_set_button.grid(column=1, row=0)

        self.search_label = tk.Label(self.mid_frame, text='Search')
        self.search_label.grid(column=0, row=0)
        self.search_entry = tk.Entry(self.mid_frame, width=40)
        self.search_entry.grid(column=1, row=0)

        self.canvas = tk.Canvas(self.bottom_frame, width=275, height=330, relief=tk.FLAT)
        self.canvas.grid(column=0, row=0)
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)

        self.logins_frame = tk.Frame(self.canvas, width=300, height=300)

        self.scrollbar = tk.Scrollbar(self.bottom_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(column=1, row=0, sticky='ns')

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.logins_frame, anchor='nw')

        self.login_objects = []

    def _on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    def add_login(self):
        row = len(self.login_objects) + 1
        new_login = LoginObj(self, row, '', '', '')
        new_login.edit_button.invoke()
        self.login_objects.append(new_login)
        self.data_logins['logins'].append(['', '', ''])

        h = self.logins_frame.winfo_height()
        self.logins_frame.configure(height=(h + 40))
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.yview_moveto(1)

    def to_set_f(self):
        self.manager_frame.grid_forget()
        self.set_frame.frame.grid()

    def import_logins(self):
        h = 0
        row = 0
        for login in self.data_logins['logins']:
            self.login_objects.append(LoginObj(self, row, login[0], login[1], login[2]))
            row += 1
            h += 40
            self.logins_frame.configure(height=h)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def decrypt(self, key):
        try:
            pyAesCrypt.decryptFile("logins.json.aes", "logins.json", key, bufferSize)
            file = open('logins.json', 'r+')
            read = file.read()
            file.close()
            os.remove("logins.json")

            logins_new = json.loads(read)
            self.data_logins = logins_new

        except ValueError:
            print('Wrong password (or file is corrupted)')

    def encrypt(self):
        file = open('logins.json', "w")
        json.dump(self.data_logins, file, indent=4)
        file.close()

        pyAesCrypt.encryptFile("logins.json", "logins.json.aes", self.data_logins['key'], bufferSize)

        os.remove("logins.json")
