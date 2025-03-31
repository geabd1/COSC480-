import cv2
import numpy as np
from PIL import Image

img = cv2.imread('/Users/tinaabdalla/Desktop/IMG_2180.JPG')

h, w, c = img.shape

# Adjust width to be even to avoid shape mismatches
if w % 2 != 0:
    w -= 1  # Reduce by 1 if odd
    img = img[:, :w]  # Crop image to even width

left_half = img[:, :w//2]

mirrored_half = cv2.flip(left_half, 1)

img_copy = img.copy()

img_copy[:, w//2:] = mirrored_half

img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)

cv2.imshow('Original Image', img)
cv2.imshow('Mirrored Image', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()