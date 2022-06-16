import os
import shutil
import json
import cv2


# name11 = {0:'pedes',1:'car',2:'bus',3:'bigtru',4:'bike',5:'elec',6:'tricycle',7:'warm',8:'fireen',9:'polic',10:'ambu',11:'excava',12:'bull',13:'crane'}
name11 = {'0':'pedes','1':'car','2':'bus','3':'bigtru','4':'bike','5':'elec','6':'tricycle','7':'warm','8':'fireen','9':'polic','10':'ambu','11':'excava','12':'bull','13':'crane'}


def readtxtToJson():
    """
    将txt文件转为标注精灵可导入识别的json文件
    """
    path = r'F:\videosLQ\DatesLQ_1\mylabels\images\outputs'
    files = os.listdir(path)
    for f in files:

        path_img = r'F:\videosLQ\DatesLQ_1\mylabels\images'
        label_img = r'F:\videosLQ\DatesLQ_1\mylabels\labels'
        filePath = os.path.join(path, f)

        imgShape = cv2.imread(os.path.join(path_img, f[:-5] + '.jpg')).shape
        # print('imgShape:',imgShape)
        objectValue = []
        with open(os.path.join(label_img, f[:-5] + '.txt'), 'r', encoding='utf-8') as rf:
            data = rf.readlines()
            for d in data:
                box = {}
                o = d.split(' ')
                box['name'] = o[0]
                if box['name'] != '14':
                    box['name'] = name11[o[0]]

                    box['bndbox'] = {}
                    box['bndbox']['xmin'] = int(o[1])
                    box['bndbox']['xmin'] = 0 if box['bndbox']['xmin'] < 0 else box['bndbox']['xmin']
                    box['bndbox']['ymin'] = int(o[2])
                    box['bndbox']['ymin'] = 0 if box['bndbox']['ymin'] < 0 else box['bndbox']['ymin']
                    box['bndbox']['xmax'] = int(o[3])
                    box['bndbox']['xmax'] = imgShape[1] if box['bndbox']['xmax'] > imgShape[1] else box['bndbox']['xmax']
                    box['bndbox']['ymax'] = int(o[4])
                    box['bndbox']['ymax'] = imgShape[0] if box['bndbox']['ymax'] > imgShape[0] else box['bndbox']['ymax']
                    objectValue.append(box)
                    # print('box::',box)
                else:
                    continue

        with open(filePath, 'r', encoding='utf-8') as rf:
            content = json.load(rf)
            content['size'] = {"width": imgShape[1], "height": imgShape[0], "depth": imgShape[2]}
            content['outputs'] = {'object': objectValue}

        # print(content)
        with open(filePath, 'w', encoding='utf-8') as wf:
            # wf.write(json.dumps(content))
            json.dump(content, wf)

if __name__ == '__main__':
    readtxtToJson()

    try:
        pass
    except:
        pass


