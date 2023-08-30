import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# 指定视频文件所在的文件夹路径
folder_path = "./wu"

# 获取文件夹中的视频文件列表
video_files = [file for file in os.listdir(folder_path) if file.endswith(".MOV")]

# 创建一个VideoFileClip对象列表
video_clips = [VideoFileClip(os.path.join(folder_path, file)) for file in video_files]

# 将视频文件列表连接起来
final_clip = concatenate_videoclips(video_clips)

# 保存合并后的视频文件
final_clip.write_videofile("merged_video.MOV", codec="libx264")
