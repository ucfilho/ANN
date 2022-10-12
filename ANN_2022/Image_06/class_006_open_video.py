import cv2
import os
print(cv2.__version__)

# you find this video here:
# https://drive.google.com/file/d/1mx3LUdeFO1-KFzClhFVwu71KWM3-s1hO/view?usp=sharing

print(os.getcwd())
path_dir = r"C:\Users\User\Documents\Atividades_andamento\computer_vision"
os.chdir(path_dir)

name_video = 'strawberry.mp4'
cap = cv2.VideoCapture(name_video)

if cap.isOpened() == False:
  print('video not found')

while cap.isOpened():
  ret,frame =cap.read()

  if ret == True:
    cv2.imshow('frame',frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
      break
  else:
    break


cap.release()
cv2.destroyAllWindows()
