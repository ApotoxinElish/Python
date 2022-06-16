'''
移动文件 到 其他目录下
将文件从一处移动（移动，不是复制）到另一个文件夹下
'''

import os
import shutil

def movefile():

    pathtxt = r'F:\datasTrain2206\labels\train'
    pathimg = r'F:\datasTrain2206Delete'

    files = os.listdir(pathimg)

    # v2x = []
    # for f in files:
    #     if f[0] == 'v':
    #         v2x.append(f)

    lenv2x = len(files)
    print(lenv2x)  # 45152
    for f in files:
        try:
            # txt_path_name = os.path.join(pathtxt, f)
            # shutil.move(txt_path_name, r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\labels')

            fi = f[:-4] + '.txt'
            # print(fi)
            path = r'F:\datasTrain2206\labels\train'
            img_path_name = os.path.join(path, fi)
            shutil.move(img_path_name, r'F:\datasTrain2206Delete')
        except:
            print(f,'失败')
            continue

if __name__ == '__main__':
    movefile()

