import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('img5.jpg')

isDown=False

ix,iy= 0,0
down_x,down_y=0,0
mouse_x,mouse_y=0,0

def draw_circle(event,x,y,flags,param):
    global ix,iy,isDown,down_x,down_y,mouse_x,mouse_y

    if event == cv2.EVENT_LBUTTONDOWN:
        down_x,down_y = x,y
        isDown=True
    
    elif event == cv2.EVENT_LBUTTONUP:
        isDown=False  
    
    elif event == cv2.EVENT_MOUSEMOVE and isDown:
        ix,iy =x,y
        mouse_x,mouse_y =x,y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        ix,iy =x,y
        
       

cv2.namedWindow('image')

R= 'value: '
cv2.createTrackbar(R,'image',255,0,nothing)
cv2.setMouseCallback('image',draw_circle)

while(1):
    img=cv2.imread('img5.jpg')

    if down_x!=0 and down_x!=0:
        start_x= min(down_x,mouse_x)
        start_y= min(down_y,mouse_y)
        end_x= max(down_x,mouse_x)
        end_y= max(down_y,mouse_y)
        r=cv2.getTrackbarPos(R,'image')
        img[start_y:end_y,start_x:end_x,2] =r

       
    cv2.imshow('image',img)
    

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'mouse position'+str(ix)+','+str(iy),(10,30),font, 1,(255,255,255),2,cv2.LINE_AA)
 
    img2 = cv2.cvtColor(img,cv2.COLOR_BGRA2BGR)
    cv2.imshow('image',img2)

    k=cv2.waitKey(1)&0xFF
    if k== 27:
        break
cv2.destroyAllWindows()
