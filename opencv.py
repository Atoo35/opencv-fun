import numpy as np
import cv2
img = cv2.imread('front.jpg',0)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
img = np.zeros((512,512,3),np.uint8)
img = cv2.line(img,(0,0),(511,511),(0,255,0),5)
					#start-end
img = cv2.rectangle(img,(384,0),(510,128),(255,0,0),3)
						#top-left bottom-right
img = cv2.circle(img,(447,63),63,(0,0,255),-1)
					 #center radius
pts = np.array([[256,300],[350,360],[210,60]],np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv2.LINE_AA)
		   #where what co-ordinates font_Type size colour thickness 
cv2.imshow('image',img)
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
cv2.waitKey(0)
cv2.destroyAllWindows()