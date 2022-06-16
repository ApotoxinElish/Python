from urllib import request
from PIL import Image
import os
import numpy as np
import requests, io

# dirpath = r"D:\车路通\Data\test"
dirpath = r"D:\车路通\LIU\数据\吊车文件"
filenames = os.listdir(dirpath)


def delete_small_img():
    remove_files = []
    for filename in filenames[:]:
        portion = os.path.splitext(filename)  # 将文件名和缀名分成俩部分
        filepath = os.path.join(dirpath, filename)

        with open(filepath, "rb") as f:
            size = len(f.read())
            print("{}图片的大小{} byte，{} kb，{} Mb".format(filename, size, size / 2 ** 10, size / 2 ** 20))
            size_kb = size / 2 ** 10
            if int(size_kb) < 5:
                print("____________ok_____________")
                # if os.path.exists(filename):
                remove_files.append(filepath)
                print("_______________%r________________: DELET welldown~", filename)
            else:
                print("-----------------continue!------------------")
                continue

    for each in remove_files:
        os.remove(each)


if __name__ == "__main__":
    delete_small_img()
