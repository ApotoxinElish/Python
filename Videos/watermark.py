import cv2


def replace_watermark(original_video_path, watermark_video_path, output_video_path):
    original_cap = cv2.VideoCapture(original_video_path)
    watermark_cap = cv2.VideoCapture(watermark_video_path)

    fps = original_cap.get(cv2.CAP_PROP_FPS)
    width = int(original_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(original_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    while original_cap.isOpened() and watermark_cap.isOpened():
        ret_original, frame_original = original_cap.read()
        ret_watermark, frame_watermark = watermark_cap.read()

        if not ret_original or not ret_watermark:
            break

        frame_replaced = frame_watermark.copy()
        frame_replaced[height // 2 : height, :] = frame_original[
            height // 2 : height, :
        ]

        out.write(frame_replaced)

    original_cap.release()
    watermark_cap.release()
    out.release()


# 示例用法
original_video_path = "merged_video.MOV"  # 原视频路径
watermark_video_path = "test2_Pro_HQ.mp4"  # 有水印的视频路径
output_video_path = "output_video.mp4"  # 输出视频路径

replace_watermark(original_video_path, watermark_video_path, output_video_path)
