from tkinter import *
import random, string


root=Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")

my_text = Text(root, width=60, height=15)
my_text.pack(pady=5)

button_frame = Frame(root)
button_frame.pack()

enter_button = Button(button_frame, text='Enter Password')
enter_button.grid(row=5, column=5)

root.mainloop()

#test for functions
from tkinter import *

#Create window
window = Tk()
window.title("1Pass")
window.geometry('350x200')

###GENERATION OF PASSWORD/PASSPHRASE
def generate_password():
    res = "Your password is: " + txt_password.get()
    lbl_password.configure(text= res)

def generate_passphrase():
    res = "Your password is: " + txt_passphrase.get()
    lbl_passphrase.configure(text= res)


##PASSWORD
#Label for password
lbl_password = Label(window, text="Your generated password section")
lbl_password.grid(column=0, row=0)
#Textbox for password
txt_password = Entry(window,width=10)
txt_password.grid(column=1, row=0)
txt_password.focus()
#Button for password
btn_password = Button(window, text="Generate your password", command=generate_password)
btn_password.grid(column=2, row=0)


##PASSPHRASE
#Label for passphrase
lbl_passphrase = Label(window, text="Your generated password section")
lbl_passphrase.grid(column=0, row=1)
#Textbox for passphrase
txt_passphrase = Entry(window,width=10)
txt_passphrase.grid(column=1, row=1)
#Button for passphrase
btn = Button(window, text="Generate your passphrase", command=generate_passphrase)
btn.grid(column=2, row=1)



window.mainloop()
