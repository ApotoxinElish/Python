import os
import shutil
import json
# import cv2


def changeLab3to1():
    '''改变v2x开源的数据中 label值 ：3（SUV、箱式货车） 改为 1（轿车）'''
    path = r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\imgs\outputs'
    files = os.listdir(path)
    for f in files:
        print(f)
        filepath = os.path.join(path, f)
        with open(filepath, 'r', encoding='utf-8') as rf:
            content = json.load(rf)
            # content['size'] = {"width": 1920, "height": 1080, "depth": 3}
            # content['outputs'] = {'object': objectValue}
            # print(content)
            # print(type(content))
            output = content['outputs']['object']
            for box in output:
                if box['name'] == "3":
                    box['name'] = '1'
            content['outputs'] = {'object': output}

        with open(filepath, 'w', encoding='utf-8') as wf:
            # wf.write(json.dumps(content))
            json.dump(content, wf)

        # break

    pass


def movejson():
    '''移动部分指定json文件到指定的目录中'''
    path1 = r'C:\Users\VRC\PyPrj\Dateproce\mydata'
    path2 = r'D:\datasTrain2206\labels\train'
    movepath = r'C:\Users\VRC\PyPrj\Dateproce\mydata_lable'

    files = os.listdir(path1)
    file2s = os.listdir(path2)

    for f in files[1:]:
        f2name = f[:-4] + '.txt'
        # if f2name not in file2s:
        #     fname = os.path.join(path1, f)
        #     shutil.move(fname, movepath)
        try:
            fname = os.path.join(path2, f2name)
            shutil.move(fname, movepath)
            # break
        except:
            continue



def biaoZhuJingLingDeJsonToTxt():
    pass


def moveImgsLabels2():
    pathtxt = r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\end0_img_json_val\outputs'
    pathimg = r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\end0_img_json_val'

    files = os.listdir(pathimg)
    print(len(files))

    for f in files[:]:
        if f[0] != 'o':
            try:
                txt_path_name = os.path.join(pathtxt, f[:-4] + '.json')
                shutil.move(txt_path_name,
                            r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\deletDatasNotTrainNotVal\Noobjs')  # 移动（非复制）

                img_path_name = os.path.join(pathimg, f)
                shutil.move(img_path_name,
                            r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\deletDatasNotTrainNotVal\Noobjs')
            except Exception as e:
                print(f, '失败', e)
                continue


def moveImgsLabels():
    pathtxt = r'D:\yolov5train\datasTrain2203_139361_16000\labels\train'
    pathimg = r'D:\yolov5train\datasTrain2203_139361_16000\images\train'

    files = os.listdir(pathtxt)

    # my2203 = []
    # for f in files:
    #     if len(f) == 12:  # if f[0] == 'v':
    #         my2203.append(f)
    #
    # # my2203 = len(my2203)
    # print(my2203)  # 45152
    # print(len(my2203))

    for f in files:
        print(f)
        try:
            txt_path_name = os.path.join(pathtxt, f)
            shutil.move(txt_path_name, r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\labels')  # 移动（非复制）

            fi = f[:-4] + '.jpg'
            # print(fi)
            img_path_name = os.path.join(pathimg, fi)
            shutil.move(img_path_name, r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\imgs')
        except:
            print(f, '失败')
            continue


def readtxtToJson():
    """
    将txt文件转为标注精灵可导入识别的json文件
    """
    path = r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\imgs\outputs'  ## 标注精灵导出后，文件夹才会有数据
    files = os.listdir(path)
    ic = 1
    for f in files:
        print(ic, ': ', f, "txt文件内容写为json")
        ic = ic + 1
        path_img = r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\imgs'
        label_img = r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\labels'
        filePath = os.path.join(path, f)

        imgShape = cv2.imread(os.path.join(path_img, f[:-5] + '.jpg')).shape
        print('imgShape:', imgShape)
        objectValue = []
        with open(os.path.join(label_img, f[:-5] + '.txt'), 'r', encoding='utf-8') as rf:
            data = rf.readlines()
            for d in data:
                box = {}
                o = d.split(' ')
                box['name'] = '1' if o[0] == "3" else o[0]
                # box['name'] = o[0]
                box['bndbox'] = {}
                box['bndbox']['xmin'] = int((float(o[1]) - float(o[3]) / 2) * imgShape[1])
                box['bndbox']['xmin'] = 0 if box['bndbox']['xmin'] < 0 else box['bndbox']['xmin']
                box['bndbox']['ymin'] = int((float(o[2]) - float(o[4]) / 2) * imgShape[0])
                box['bndbox']['ymin'] = 0 if box['bndbox']['ymin'] < 0 else box['bndbox']['ymin']
                box['bndbox']['xmax'] = int((float(o[1]) + float(o[3]) / 2) * imgShape[1])
                box['bndbox']['xmax'] = imgShape[1] if box['bndbox']['xmax'] > imgShape[1] else box['bndbox']['xmax']
                box['bndbox']['ymax'] = int((float(o[2]) + float(o[4]) / 2) * imgShape[0])
                box['bndbox']['ymax'] = imgShape[0] if box['bndbox']['ymax'] > imgShape[0] else box['bndbox']['ymax']
                objectValue.append(box)

        with open(filePath, 'r', encoding='utf-8') as rf:
            content = json.load(rf)
            content['size'] = {"width": imgShape[1], "height": imgShape[0], "depth": imgShape[2]}
            content['outputs'] = {'object': objectValue}

        # print(content)
        with open(filePath, 'w', encoding='utf-8') as wf:
            # wf.write(json.dumps(content))
            json.dump(content, wf)


def deletymax1080():
    path = r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\imgs\outputs'
    files = os.listdir(path)
    # print(files[56:187])
    imgw,imgh = 1920,1080

    ca = [{				"name": "6",
				"bndbox": {
					"xmin": 426,
					"ymin": 274,
					"xmax": 634,
					"ymax": 429
				}			},			{
				"name": "6",				"bndbox": {
					"xmin": 390,
					"ymin": 200,					"xmax": 552,
					"ymax": 329
				}			},			{
				"name": "6",
				"bndbox": {
					"xmin": 293,
					"ymin": 157,
					"xmax": 397,
					"ymax": 288				}			}]

    for f in files[1:8]:
        print(f)

        filepath = os.path.join(path, f)
        with open(filepath, 'r', encoding='utf-8') as rf:
            content = json.load(rf)
            output = content['outputs']['object']
            print(type(output))
            outputNew = []

            for box in output:
                box['bndbox']['ymax'] = imgh if -5<box['bndbox']['ymax']-imgh<5 else box['bndbox']['ymax']
                box['bndbox']['ymin'] = 0 if -5<box['bndbox']['ymin']<5 else box['bndbox']['ymin']
                box['bndbox']['xmax'] = imgw if -5<box['bndbox']['xmax']-imgw<5 else box['bndbox']['xmax']
                box['bndbox']['xmin'] = 0 if -5<box['bndbox']['xmin']<5 else box['bndbox']['xmin']
                if box['bndbox']['ymax'] < 1070:
                    outputNew.append(box)

            outputNew.extend(ca)
            # outputNew.append(ca)

            content['outputs']['object'] = outputNew

        with open(filepath, 'w', encoding='utf-8') as wf:
            # wf.write(json.dumps(content))
            json.dump(content, wf)
        # break


def deletymax640():
    path = r'D:\yolov5train\datasTrain2203_139361_16000\xiuZheng\imgs\outputs'
    files = os.listdir(path)
    # print(files[56:187])
    # imgw,imgh = 1920,1080
    imgw,imgh = 640,640

    ca = [
        {
            "name": "7",
            "bndbox": {
                "xmin": 335,
                "ymin": 337,
                "xmax": 350,
                "ymax": 363
            }
        },
        {
            "name": "7",
            "bndbox": {
                "xmin": 354,
                "ymin": 324,
                "xmax": 369,
                "ymax": 350
            }
        },
        {
            "name": "7",
            "bndbox": {
                "xmin": 378,
                "ymin": 308,
                "xmax": 391,
                "ymax": 332
            }
        },
        {
            "name": "7",
            "bndbox": {
                "xmin": 1460,
                "ymin": 263,
                "xmax": 1475,
                "ymax": 287
            }
        },
        {
            "name": "7",
            "bndbox": {
                "xmin": 1484,
                "ymin": 273,
                "xmax": 1497,
                "ymax": 297
            }
        },
        {
            "name": "7",
            "bndbox": {
                "xmin": 1507,
                "ymin": 281,
                "xmax": 1522,
                "ymax": 308
            }
        }]

    for f in files[24:44]:
        print(f)

        filepath = os.path.join(path, f)
        with open(filepath, 'r', encoding='utf-8') as rf:
            content = json.load(rf)
            content['outputs']['object'] = []
            output = content['outputs']['object']
            print(type(output))
            outputNew = []

            for box in output:
                box['bndbox']['ymax'] = imgh if -5<box['bndbox']['ymax']-imgh<5 else box['bndbox']['ymax']
                box['bndbox']['ymin'] = 0 if -5<box['bndbox']['ymin']<5 else box['bndbox']['ymin']
                box['bndbox']['xmax'] = imgw if -5<box['bndbox']['xmax']-imgw<5 else box['bndbox']['xmax']
                box['bndbox']['xmin'] = 0 if -5<box['bndbox']['xmin']<5 else box['bndbox']['xmin']
                outputNew.append(box)
                if box['bndbox']['ymax'] < 1070:
                    outputNew.append(box)

            outputNew.extend(ca)
            # outputNew.append(ca)

            content['outputs']['object'] = outputNew

        with open(filepath, 'w', encoding='utf-8') as wf:
            # wf.write(json.dumps(content))
            json.dump(content, wf)
        # break


if __name__ == '__main__':
    movejson()
    pass
