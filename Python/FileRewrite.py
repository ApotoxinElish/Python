import os


def fileRewrite():
    os.chdir('D:/MyFile/PlayList')
    folders = os.listdir()

    for folder in folders:# zhongwen
        videos = os.listdir(folder)# luanma
        for video in videos:
            try:
                video_name = folder + ' 第' + video.split('.')[-1].zfill(2) +'集 超清(720P).mp4'
                os.rename(os.path.join(folder, video, video + '.mp4'), os.path.join(folder, video_name))
                os.rmdir(os.path.join(folder, video))
                print(video_name + ' is OK')
            except:
                pass


if __name__ == '__main__':
    fileRewrite()
