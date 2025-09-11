import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('messi6.jpg')

drawing=False
mode= True
ix,iy=-1,-1

font = cv2.FONT_HERSHEY_SIMPLEX


def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode== True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode== True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

img[300:400,300:400,2]=255


cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)

while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k== ord('m'):
         mode=not mode
    elif k==27:
        break
cv2.destroyAllWindows()