''' 标注精灵的json文件转txt'''
import os
import json
import shutil


def json2txt():
    ''' 标注精灵的json文件转txt'''

    path = r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\end6_img_json-lqnight\outputs'
    desPath = r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\end6_img_json-lqnight\outputs'
    imgw, imgh = 1920, 1080

    files = os.listdir(path)
    ic = 1
    for f in files[:1]:
        print(ic, ':  ', f)
        ic = ic + 1
        json_path_name = os.path.join(path, f)
        with open(json_path_name, 'r', encoding='utf-8') as rf:
            rf = json.load(rf)
            objs = rf['outputs']['object']
            boxs = []
            for o in objs:
                id = o['name']
                xmin = o['bndbox']['xmin']
                ymin = o['bndbox']['ymin']
                xmax = o['bndbox']['xmax']
                ymax = o['bndbox']['ymax']
                ymax = imgh if -5 < ymax - imgh < 5 else ymax
                ymin = 0 if -5 < ymin < 5 else ymin
                xmax = imgw if -5 < xmax - imgw < 5 else xmax
                xmin = 0 if -5 < xmin < 5 else xmin
                x = (xmin + xmax) / 2 / imgw
                y = (ymin + ymax) / 2 / imgh
                w = (xmax - xmin) / imgw
                h = (ymax - ymin) / imgh
                x = str(x) if len(str(x)) <= 7 else str(x)[:7]
                y = str(y) if len(str(y)) <= 7 else str(y)[:7]
                w = str(w) if len(str(w)) <= 7 else str(w)[:7]
                h = str(h) if len(str(h)) <= 7 else str(h)[:7]
                box = id + ' ' + x + ' ' + y + ' ' + w + ' ' + h + '\n'
                boxs.append(box)
            boxs[-1] = boxs[-1].replace('\n', '')

        txt_path_name = os.path.join(path, f[:-5] + '.txt')
        with open(txt_path_name, 'w', encoding='utf-8') as wf:
            wf.writelines(boxs)

        break


if __name__ == '__main__':
    json2txt()
    pass
