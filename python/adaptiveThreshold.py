import sys
import cv2
import numpy as np

image = cv2.imread(sys.argv[1], 0)

image = cv3.GaussianBlur(image, (3, 3), 0)

type_of_thresh = int(sys.argv[2])

if type_of_thresh == 0:
	thresh = cv2.threshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
elif type_of_thresh == 1:
	thresh = cv2.threshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 3, 5)
elif type_of_thresh == 2:
	thresh = cv2.threshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_TRUNC, 3, 5)
elif type_of_thresh == 3:
	thresh = cv2.threshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_TOZERO, 3, 5)
else:
	thresh = cv2.threshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_TOZERO_INV, 3, 5)

cv2.imwrite(sys.argv[1], thresh)