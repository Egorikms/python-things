import tkinter as tk
from tkinter import *
from tkinter import messagebox 

def da():
    da_1 = str(chtoto_wod.get())
    da_2 = str(chtoto_wod2.get())

    if da_1 == "чтото" and da_2 == "ещё чтото":
        messagebox.showinfo("  ", "Ты молодец)))")
    elif da_1 == "xnjnj" and da_2 == "to` xnjnj":
        messagebox.showinfo(" ", "Смени расскладку)))")
    else:
        messagebox.showinfo("  ", "Ты лох, пробуй ещё раз")

window = Tk()
window.title("нет")
window.geometry('400x300')

frame = Frame(
    window,
    padx = 10,
    pady = 10,
) 
frame.pack(expand=True)

chtoto = Label(
    frame,
    text = "Введи чтото "
)
chtoto.grid(row = 3, column = 1)

chtoto1 = Label(
    frame,
    text = "Введи ещё чтото "
)
chtoto1.grid(row = 4, column = 1)

chtoto_wod = Entry(
    frame,
)
chtoto_wod.grid(row=3, column=2)

chtoto_wod2 = Entry(
    frame,
)
chtoto_wod2.grid(row=4, column=2)

button = Button(
    frame, 
    text = "Рандом",
    command=da
)
button.grid(row=5, column=1)

window.mainloop()