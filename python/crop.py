import sys
import cv2
import numpy as np

image = cv2.imread(sys.argv[1])

cv2.imwrite(sys.argv[1], image[int(sys.argv[2]) : int(sys.argv[3]), int(sys.argv[4]) : int(sys.argv[5])])