import cv2
import os
import time
print(cv2.__version__)

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
    time.sleep(1/20)
    cv2.imshow('frame',frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
      break
  else:
    break


cap.release()
cv2.destroyAllWindows()