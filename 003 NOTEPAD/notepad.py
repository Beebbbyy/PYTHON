from tkinter.constants import ANCHOR, END, INSERT, LEFT, TRUE
from tkinter.filedialog import *
import tkinter as tk
from tkinter.font import Font
from typing import Text

def saveFile():
    new_file = asksaveasfile(mode='w', filetype = [('text files' ,'.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, asksaveasfile.END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode='r', filetype=[('text files', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT,content)

def clearFile():
    entry.delete(1.0,END)


canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notpad")
canvas.config(bg="white")
top= tk.Frame(canvas)
top.pack(anchor= 'nw',padx =10, pady=5)

b1 = tk.Button(canvas, text ="Open", bg="white", command= openFile)
b1.pack(in_ = top ,side=LEFT)

b2 = tk.Button(canvas, text ="Save", bg="white", command= saveFile)
b2.pack(in_ = top ,side=LEFT)

b3 = tk.Button(canvas, text ="Clear", bg="white", command= clearFile)
b3.pack(in_ = top ,side=LEFT)

b4 = tk.Button(canvas, text ="Exit", bg="white",command= exit)
b4.pack(in_ = top ,side=LEFT)

entry = tk.Text(canvas,wrap= tk.WORD, bg="#F9DDA4", font = ("poppins", 15))
entry.pack(padx=10, pady=5, expand= TRUE, fill = tk.BOTH)

canvas.mainloop()