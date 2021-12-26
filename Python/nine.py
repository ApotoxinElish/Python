from PIL import Image
import os

__author__ = '鱼C-小师妹'

DIR_NAME = os.path.dirname(os.path.abspath(__file__))

def fill_images(image):
    width,height = image.size
    side = max(width,height)
    new_image = Image.new(image.mode,(side,side),color = 'white')
    if width > height:
        new_image.paste(image,(0,int((side - height) / 2)))
    else:
        new_image.paste(image,(int((side - width) / 2),0))
    return new_image

def cut_images(image):
    width,height = image.size
    one_third_width = int(width / 3)
    box_
def fishcRun():
    file_path = os.path.join(DIR_NAME,'demo.jpg')
    image = Image.open(file_path)
    image = fill_images(image)
    image_list = cut_images(image)
    print('程序结束啦！')

if __name__ == '__main__':
    fishcRun()
