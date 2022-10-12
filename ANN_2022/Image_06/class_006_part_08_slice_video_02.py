import cv2
import os
import time
print(cv2.__version__)

print(os.getcwd())
path_dir = r"C:\Users\User\Documents\Atividades_andamento\computer_vision"
os.chdir(path_dir)

name_video = 'strawberry.mp4'
video_cap = cv2.VideoCapture(name_video)
num_frames = int(video_cap.get(cv2. CAP_PROP_FRAME_COUNT))

success,image = video_cap.read()
count, k = 0, 0
fator = 100 

while success:
  count += 1
  if count % fator == 0:
    k += 1
    cv2.imwrite("frame%d.jpg" % k, image)     # save frame as JPEG file      
  success,image = video_cap.read()
  # print('Read a new frame: ', success)
  

print('count=',count)
print('video count =',num_frames)
