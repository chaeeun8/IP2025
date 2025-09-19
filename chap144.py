import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('opencv_logo.png')

k=15

kernel = np.ones((k,k),np.float32)/(k*k)
dst = cv2.filter2D(img,-1,kernel)

blur = cv2.blur(img,(k,k))
G_blur = cv2.GaussianBlur(img,(k,k),0)
median = cv2.medianBlur(img,k)

#plt.subplot(121),plt.imshow(dst),plt.title('3x3')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('blur')
plt.xticks([]), plt.yticks([])
#plt.subplot(121),plt.imshow(G_blur),plt.title('Gaussian')
#plt.xticks([]), plt.yticks([])
plt.subplot(121),plt.imshow(median),plt.title('median')
plt.xticks([]), plt.yticks([])
plt.show()