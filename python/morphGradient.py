import sys
import cv2
import numpy as np

img = cv2.imread(sys.argv[1])
kernel = np.ones((int(sys.argv[2]), int(sys.argv[2])), np.uint8)
morphGradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imwrite(sys.argv[1], morphGradient)