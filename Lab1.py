import cv2 
import numpy as np

img = cv2.imread('/Users/tinaabdalla/Desktop/IMG_2180.JPG')

b = 25
x, y = 1400, 800 #column, row


img = cv2.resize(img, (1400, 800))
img[y-100:y-50, x-100:x-50] = [0, 0, 255]
img[y-600:y-550, x-800:x-750] = [174, 163, 230]
print("img.Shape: ", img.shape)

cv2.imshow('win', img)

#img[x1:x2, y1:y2] = img [b,g,r] in order to alter a specific part of picture

#img = cv2.resize(img, (0,0), fx=0.5, fy =0.5)

#img = cv2.flip(img, 1) #flip image 1 on x acis

#cv2.setMouseCallback("win", click_event) #mouse callback


for i in range (100, 700):
    dif0 = (proj3[i, 10111][0]) - proj3([i, 989][0]) /20
    dif1 = (proj3[i, 10111][1]) - proj3([i, 989][1]) /20
    dif3 = (proj3[i, 10111][2]) - proj3([i, 989][2]) /20
    for j in range (990, 1010):
        proj3[i, j+1][0]= proj3[i, j][0] + dif0
        proj3[i, j+1][1]= proj3[i, j][1] + dif0
        proj3[i, j+1][2]= proj3[i, j][2] + dif0



cv2.waitKey(0)
cv2.destroyAllWindows()

#print(img)



