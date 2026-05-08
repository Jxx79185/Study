from moviepy.editor import VideoFileClip, AudioFileClip

def merge_video_audio(video_path, audio_path, output_path):
    try:
        # 加载视频（无音频）
        video = VideoFileClip(video_path)
        # 加载音频
        audio = AudioFileClip(audio_path)
        # 将音频附加到视频
        video_with_audio = video.set_audio(audio)
        # 输出合并后的文件
        video_with_audio.write_videofile(
            output_path,
            codec="libx264",  # 通用视频编码
            audio_codec="aac",  # 通用音频编码
            threads=4,          # 加速处理
            verbose=False       # 关闭冗余日志
        )
        print(f"合并成功！文件已保存至: {output_path}")
    except Exception as e:
        print(f"合并失败: {e}")
    finally:
        # 释放资源
        if 'video' in locals():
            video.close()
        if 'audio' in locals():
            audio.close()

# 使用示例
merge_video_audio(
    video_path="video.m4s",
    audio_path="audio.m4s",
    output_path="合并视频.mp4"
)