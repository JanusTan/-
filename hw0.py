'''
programmer:Ryan Tan
requirement of the homework:
1.segment
2.caculate the number of cell
3.and compute the HuMoment
'''

import numpy as np
import cv2

#function to write number of full cell in the source picture and compute seven HuMoment
def writetxt(p,Hu):
  with open("result.txt","a") as f:
     f.write("\n-------------------------------------segmentLine-----------------------------------------\n")
     f.write("Number:"+str(p)+'\n')
     for j in range(7):
      f.write("HU"+str(j)+':'+str(HU[j])+'\n')
     

img = cv2.imread('source.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.medianBlur(gray, 5)
ret, thresh = cv2.threshold(img2, 105, 255,cv2.THRESH_BINARY)
#THRESH_BINARY is perfect need no more erode and dialte
#kernel = np.ones((2,2),np.uint8)
#erosion = cv2.erode(thresh,kernel,iterations = 3)
#dilation = cv2.dilate(erosion,kernel,iterations = 1)
img3,contours,hierarchy = cv2.findContours(thresh, 1, 2)

for i in range(len(contours)-1):
 
 coor0=contours[i]
 coor=coor0[0]
 si=str(i+1)
 #mask the cell which has been segmented 
 cv2.putText(img,si,(coor[0][0],coor[0][1]),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
 img4 = cv2.drawContours(img, contours, i, (0,255,0), 1)
 M = cv2.moments(coor0)
 HU=cv2.HuMoments(M)
 writetxt(i,HU)


cv2.imshow('result',img4)
cv2.waitKey(0)
