from moviepy.editor import concatenate_videoclips, VideoFileClip
import os

# 视频文件的放置目录
video_dir = "./wu"

# 获取目录下的所有文件
files = os.listdir(video_dir)

# 用于存放视频片段的列表
clips = []

for file in files:
    print(file)
    # 只处理mov文件
    if file.endswith(".MOV"):
        # 读取视频文件，并添加到clips列表中
        clip = VideoFileClip(os.path.join(video_dir, file))
        # 如果视频的分辨率不是1920x1080，则调整分辨率
        if clip.size != [1920, 1080]:
            clip = clip.resize(height=1080)
        clips.append(clip)

# 使用concatenate_videoclips函数来连接所有的视频片段
final_clip = concatenate_videoclips(clips)

# 导出最后的视频
final_clip.write_videofile("merged_video.MOV", codec="libx264")
