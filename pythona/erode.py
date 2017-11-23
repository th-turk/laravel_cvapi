import sys
import cv2
import numpy as np

img = cv2.imread(sys.argv[1])
kernel = np.ones((int(sys.argv[2]), int(sys.argv[2])), np.uint8)
erosion = cv2.erode(img,kernel,iterations = int(sys.argv[3]))

cv2.imwrite(sys.argv[1], erosion)