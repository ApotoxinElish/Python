# coding=utf-8
from tkinter import *
import tkinter as tk
from tkinter import Canvas as C
import tkinter, time, decimal, math, string
import tkinter.messagebox  # 这个是消息框，对话框的关键
import tkinter.font as tkFont
import os
from PIL import Image
from PIL import ImageFile

import imagehash
import threading
import hashlib


def thread_it(func, *args):
    '''将函数放入线程中执行'''
    # 创建线程
    t = threading.Thread(target=func, args=args)
    # 守护线程
    t.setDaemon(True)
    # 启动线程
    t.start()


def clear():
    if tkinter.messagebox.askokcancel('提示', '确认结束吗'):
        root.quit()


def compare_image_with_hash(image_file_name_1, image_file_name_2, max_dif=0):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    hash_1 = None
    hash_2 = None
    image_file1 = open(image_file_name_1, 'rb').read()
    Has = hashlib.md5(image_file1).hexdigest()
    image_file2 = open(image_file_name_2, 'rb').read()
    Has1 = hashlib.md5(image_file2).hexdigest()
    # if image_file1 != image_file2:
    #     return False
    with open(image_file_name_1, 'rb') as fp:
        hash_1 = imagehash.average_hash(Image.open(fp))
    with open(image_file_name_2, 'rb') as fp:
        hash_2 = imagehash.average_hash(Image.open(fp))  # 对比图片是否一样
    dif = hash_1 - hash_2
    if dif < 0:
        dif = -dif
    if dif <= max_dif:
        return True
    else:
        return False


com_path = [""]

compath = {}  # 字典


def get_all(path):
    # path =r'D:\Test3'
    paths = os.listdir(path)  # 列出指定路径下的所有目录和文件
    for i in paths:
        com_path = os.path.join(path, i)
        # print(com_path)
        if os.path.isdir(com_path):
            get_all(com_path)  # 如果该路径是目录，则调用自身方法
        elif os.path.isfile(com_path):
            # print(com_path.split(".")[-1])
            if com_path.split(".")[-1] in ['jpg', 'png', 'bmp', 'tif', 'gif', 'pcx', 'tga', 'exif', 'fpx', 'svg', 'psd',
                                           'cdr', 'pcd', 'dxf', 'ufo', 'eps', 'ai', 'raw', 'WMF', 'webp', 'avif'
                                                                                                          'JPG', 'PNG',
                                           'BMP', 'TIF', 'GIF', 'PCX', 'TGA', 'EXIF', 'FPX', 'SVG', 'PSD', 'CDR', 'PCD',
                                           'DXF', 'UFO', 'EPS', 'AI', 'RAW', 'WMF', 'WEBP', 'AVIF'
                                           ]:
                com_path_T = {com_path.split('\\')[-1]: com_path}
                compath.update(com_path_T)
            # print(com_path.split('\\')[-1],"======",com_path)


get_all(path=r'D:\车路通\手推车文件')
keyList = []
valueList = []
print(len(compath))
for key in compath.keys():
    keyList.append(key)
for value in compath.values():
    valueList.append(value)


def getuser():
    line_new = open("test.txt", 'w')
    FlagNum = 0
    strInfoT = "正在循环对比..."
    tkinter.Label(root, text=strInfoT).place(x=50, y=70)
    for i in range(0, len(valueList), 1):
        strInfoNum = "已完成" + str(i + 1) + "个..."
        tkinter.Label(root, text=strInfoNum).place(x=160, y=70)
        for j in range(1, len(valueList), 1):
            if i != j and i < j:
                if compare_image_with_hash(valueList[i], valueList[j], 0) == True:
                    FlagNum = 1
                    line_new.write(valueList[i] + "和" + valueList[j] + "相同\n")
    line_new.close()
    if FlagNum == 1:
        tkinter.messagebox.showwarning('警告', '图片相同,相同照片以保持至根目录下的test.txt中，请确认！！')
    elif FlagNum == 0:
        tkinter.messagebox.showwarning('提示', '当前路径下没有相同的图片！')
    else:
        tkinter.messagebox.showwarning('异常', '异常情况！')


root = tkinter.Tk()  # 创建窗口对象的背景色
root.geometry("280x150+600+200")
root.title("图片筛查工具")
strInfo = "需要循环比较 " + str(len(compath)) + " 个文件,请稍等！"
tkinter.Label(root, text=strInfo).place(x=50, y=40)
tkinter.Button(root, text="开始筛查", command=lambda: thread_it(getuser)).place(x=50, y=100)  # command绑定获取文本框内容方法
tkinter.Button(root, text="结束筛查", command=clear).place(x=170, y=100)  # command绑定获取文本框内容方法
root.mainloop()  # 进入主循环
