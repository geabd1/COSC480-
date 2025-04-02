import cv2
import numpy as np

def remove_background(im, stp):
    for j in range(5, 650, 1):
        for i in range(10, 1190, 1):
            if im[j, i, 2] < stp or im[j, i, 0] > 4 * stp: 
                im[j, i] = (206, 150, 200) 

img = cv2.imread('/Users/tinaabdalla/Desktop/IMG_2180.JPG')

im = cv2.resize(img, (1200, 700))

stp = 50

remove_background(im, stp)

cv2.imshow('Processed Image', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
