import cv2
import os
import datetime
print(cv2.__version__)

print(os.getcwd())
path_dir = r"C:\Users\User\Documents\Atividades_andamento\computer_vision"
os.chdir(path_dir)

name_video = 'strawberry.mp4'
video = cv2.VideoCapture(name_video)

# count the number of frames
frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)
 
# calculate duration of the video
seconds = round(frames / fps)
video_time = datetime.timedelta(seconds=seconds)
print(f"duration in seconds: {seconds}")
print(f"video time: {video_time}")
print('frame per seconds:',fps)
print('numeber of frames:',frames)
