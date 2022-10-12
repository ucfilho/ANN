import cv2
import os
print(cv2.__version__)

print(os.getcwd())
path_dir = r"C:\Users\User\Documents\Atividades_andamento" #computer_vision\"
os.chdir(path_dir)

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# fourcc in fedora *'XVID'
#        in windows *'DIVX'
#        in McOS *'XVID'
nframes = 20 # frames per second
writer = cv2.VideoWriter('test_video.mp4',cv2.VideoWriter_fourcc(*'DIVX'),nframes,(width,height))
while True:
  ret,frame =cap.read()
  #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  #cv2.imshow('frame',gray)
  writer.write(frame)
  cv2.imshow('frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
writer.release()
cv2.destroyAllWindows()