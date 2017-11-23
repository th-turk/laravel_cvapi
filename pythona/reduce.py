import sys
import cv2
import numpy as np

image = cv2.imread(sys.argv[1])

img_scaled = cv2.resize(image, None, fx=float(sys.argv[2]), fy=float(sys.argv[3]))

cv2.imwrite(sys.argv[1], img_scaled)