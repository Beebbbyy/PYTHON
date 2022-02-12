from tkinter import * 
#from tkinker.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string =strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

label= Label(root,font=("ds-digitial",100), background="black", foreground="yellow")
label.pack(anchor='center')
time()

mainloop()