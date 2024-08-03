from tkinter import *

root = Tk()

logo = Label(root, text="Python-Calculator")
logo.grid(column=0, row=0)

numberSeven = Button(root, pady=30, padx=30, text="7")
numberSeven.grid(column=0, row=1)

root.mainloop()