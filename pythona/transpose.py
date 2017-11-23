import sys
import cv2
import numpy as np

image = cv2.imread(sys.argv[1])

transpose = cv2.transpose(image)

cv2.imwrite(sys.argv[1], transpose)