import sys
import cv2
import numpy as np

image = cv2.imread(sys.argv[1], 0)

type_of_thresh = int(sys.argv[4])

if type_of_thresh == 0:
	ret, thresh = cv2.threshold(image, int(sys.argv[2]), int(sys.argv[3]), cv2.THRESH_BINARY)
elif type_of_thresh == 1:
	ret, thresh = cv2.threshold(image, int(sys.argv[2]), int(sys.argv[3]), cv2.THRESH_BINARY_INV)
elif type_of_thresh == 2:
	ret, thresh = cv2.threshold(image, int(sys.argv[2]), int(sys.argv[3]), cv2.THRESH_TRUNC)
elif type_of_thresh == 3:
	ret, thresh = cv2.threshold(image, int(sys.argv[2]), int(sys.argv[3]), cv2.THRESH_TOZERO)
else:
	ret, thresh = cv2.threshold(image, int(sys.argv[2]), int(sys.argv[3]), cv2.THRESH_TOZERO_INV)	

cv2.imwrite(sys.argv[1], thresh)