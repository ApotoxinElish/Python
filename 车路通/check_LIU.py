import os
import tkinter as tk
# from tkinter import *
# import tkinter.messagebox
from PIL import Image, ImageTk

PATH = r'D:\车路通\LIU\数据\警车文件'

root = tk.Tk()
# root.state("zoomed")
img_names = os.listdir(PATH)

root.title("图片检查 - " + PATH.split('\\')[-1])
index = -1
img = tk.Label(root)

img.grid(column=0, row=0)


def showImg(index):
    load = Image.open(os.path.join(PATH, img_names[index]))
    resized_image = load.resize((800, 600), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    img.config(image=photo)
    # img(image=photo)
    img.photo_ref = photo
    img.grid()
    # root.update_idletasks()


def nextImg():
    global index  # , label1, root
    index += 1
    showImg(index)


def lastImg():
    global index
    index -= 1
    showImg(index)


def deleteImg():
    global index
    os.remove(os.path.join(PATH, img_names.pop(index)))
    index -= 1
    nextImg()


def uncertain():
    uncertain_path = PATH + '不确定'
    try:
        os.mkdir(uncertain_path)
    except:
        pass
    global index
    name = img_names.pop(index)
    os.rename(os.path.join(PATH, name), os.path.join(uncertain_path, name))
    index -= 1
    nextImg()


def on_closing():
    with open(os.path.join('temp.txt'), 'w') as fp:
        fp.write(str(index - 1))
    root.destroy()


def main():
    canvas = tk.Canvas(root, width=500)

    tk.Button(canvas, text='上一张', font=('微软雅黑', 12), width=12, heigh=3, command=lastImg).grid(row=0, column=0)
    tk.Button(canvas, text='下一张', font=('微软雅黑', 12), width=12, heigh=3, command=nextImg).grid(row=0, column=1)
    tk.Button(canvas, text='不确定', font=('微软雅黑', 12), bg='orange', width=12, heigh=3, command=uncertain).grid(row=0,
                                                                                                             column=2)
    tk.Button(canvas, text='删除', font=('微软雅黑', 12), bg='red', width=12, heigh=3, command=deleteImg).grid(row=0,
                                                                                                         column=3)
    canvas.grid(row=1)

    try:
        with open('temp.txt', 'r') as fp:
            global index
            index = int(fp.read())
    except:
        pass
    nextImg()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()
