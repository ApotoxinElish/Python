from tkinter import *

master = Tk()

theLB = Listbox(master, selectmode=EXTENDED, height=11)
theLB.pack()

for item in range(11):
    theLB.insert(END, item)

mainloop()
