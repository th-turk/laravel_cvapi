import sys
import cv2
import numpy as np

img = cv2.imread(sys.argv[1])
kernel = np.ones((int(sys.argv[2]), int(sys.argv[2])), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imwrite(sys.argv[1], opening)

