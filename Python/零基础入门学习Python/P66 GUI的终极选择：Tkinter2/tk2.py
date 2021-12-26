from tkinter import *

root = Tk()

photo = PhotoImage(file="chaos_token1.png")
theLabel = Label(root,
                 text="学 Python\n到 FishC",
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 font=("微软雅黑", 20),
                 fg="black")
theLabel.pack()

mainloop()
