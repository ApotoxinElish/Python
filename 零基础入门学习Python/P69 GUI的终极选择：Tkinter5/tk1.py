from tkinter import *

master = Tk()

theLB = Listbox(master, selectmode=EXTENDED,)
theLB.pack()

for item in ["鸡蛋", "鸭蛋", "鹅蛋", "李狗蛋"]:
    theLB.insert(END, item)

theButton = Button(master, text="删除它",
                   command=lambda x=theLB: x.delete(ACTIVE))
theButton.pack()

mainloop()
