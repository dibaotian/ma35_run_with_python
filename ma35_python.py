import av
import os
import time



# output_dir='output'
# output_file = 'output.mp4'
# if not os.path.exists(output_dir):  
#     os.makedirs(output_dir)  

# # 打开输出文件
# output_container = av.open(output_file, 'w')

input_file = '/home/xilinx/Documents/minx/videos/bbb_sunflower_1080p_60fps_normal.mp4'

# 打开输入文件
input_container = av.open(input_file)

# 选择视频流
video_stream = input_container.streams.video[0]
# av.Codec('h264_ama', 'r').create()  # 指定AMD卡支持的解码器

# 创建一个解码器实例
decoder = av.CodecContext.create('h264_ama','r')


# 使用解码器打开视频流
video_stream.decode(codec=decoder)

# 现在可以遍历解码后的帧
for frame in video_stream:
    # 处理帧
    pass

# 关闭容器
input_container.close()





# video_stream = next(s for s in input_container.streams if s.type == 'video') 
# # video_stream.codec_context.codec_id = 'libx264' 
# # video_stream.codec_context.codec_id = 'h264_ama' 

# # 设置编码参数
# video_stream.codec_context.bit_rate = 1000000
# video_stream.codec_context.frame_rate = 30


# # 获取输入文件中的视频流和音频流
# input_video_stream = next(s for s in input_container.streams if s.type == 'video')
# input_audio_stream = next(s for s in input_container.streams if s.type == 'audio')

# # 添加视频流到输出文件
# output_video_stream = output_container.add_stream(template=input_video_stream)

# # 添加音频流到输出文件
# output_audio_stream = output_container.add_stream(template=input_audio_stream)

# # 遍历输入文件中的每一帧
# for packet in input_container.demux(input_container.streams):
#     # 如果是视频流
#     if packet.stream == input_video_stream:
#         # 解码视频帧
#         frame = packet.decode()
#         # 编码视频帧
#         encoded_frame = output_video_stream.encode(frame)
#         # 将编码后的帧写入输出文件
#         output_container.mux(encoded_frame)
#     # 如果是音频流
#     elif packet.stream == input_audio_stream:
#         # 解码音频帧
#         frame = packet.decode()
#         # 编码音频帧
#         encoded_frame = output_audio_stream.encode(frame)
#         # 将编码后的帧写入输出文件
#         output_container.mux(encoded_frame)

# 关闭输出文件
# output_container.close()
