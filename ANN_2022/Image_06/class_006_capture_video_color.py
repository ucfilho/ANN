import cv2
print(cv2.__version__)

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
  ret,frame =cap.read()
  #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  #cv2.imshow('frame',gray)
  cv2.imshow('frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()