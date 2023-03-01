import cv2 
cam=cv2.VideoCapture(0)
while 1:
   _,frame=cam.read()
   cv2.imshow("camera",frame)
   cv2.waitKey(1)
