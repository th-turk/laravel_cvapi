import sys
import numpy as np
import cv2


image = cv2.imread(sys.argv[1])

cv2.imwrite(sys.argv[1], cv2.medianBlur(image, int(sys.argv[2])))