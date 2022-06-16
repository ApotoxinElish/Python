import os, time, hashlib

from PIL import Image
import imagehash


def getmd5(file):
    if not os.path.isfile(file):
        return
    fd = open(file, 'rb')

    try:
        hash_1 = imagehash.average_hash(Image.open(fd))
    except:
        fd.close()
        os.remove(file)
        return
    # md5 = hashlib.md5()
    # md5.update(fd.read())

    fd.close()
    # return md5.hexdigest()
    return hash_1


if __name__ == "__main__":
    allfile = []
    md5list = []
    list_delete = []

    start_time = time.time()
    path = r'D:\车路通\LIU\数据\吊车文件'  # 只需要替换这个数据集的路径即可

    for filepath, dir, filelist in os.walk(path):
        for filename in filelist:
            allfile.append(os.path.join(filepath, filename))

    # 根据MD5值比较
    for photo in allfile:
        md5sum = getmd5(photo)
        if md5sum not in md5list:
            md5list.append(md5sum)
        else:
            list_delete.append(photo)
    print('重复的照片有:', list_delete)
    print("重复的照片有 %r 张~" % len(list_delete))

    # 删除图片
    for i in range(len(list_delete)):
        try:
            os.remove(list_delete[i])
        except:
            pass

    end_time = time.time()

    print("总共耗时：", end_time - start_time)

# (80641, 80577), (81175, 80950)
