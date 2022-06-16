import os

PATH_MD5 = r'D:\车路通\手推车文件md5'
PATH_AHASH = r'D:\车路通\手推车文件average_hash'
PATH_PHASH = r'D:\车路通\手推车文件phash'
PATH_DHASH = r'D:\车路通\手推车文件dhash'


def main():
    files1 = os.listdir(PATH_PHASH)
    files2 = os.listdir(PATH_AHASH)
    different_file = []
    for each in files1:
        if each not in files2:
            different_file.append(each)
    print(len(different_file))
    print(different_file)


PATH = r'D:\车路通\LIU\数据'


def test():
    countDic = {}
    file_list = os.listdir(PATH)

    for each in file_list:
        directory = os.path.join(PATH, each)
        if os.path.isdir(directory):
            count = len(os.listdir(directory))
            countDic[each[:-2]] = count

    with open(os.path.join(PATH, 'README.txt'), 'w') as fp:
        for keys in countDic:
            # print(countDic[keys])
            fp.write(keys + ' - ' + str(countDic[keys]) + '\n')


if __name__ == "__main__":
    # main()
    test()
