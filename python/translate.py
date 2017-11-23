import sys
import cv2
import numpy as np

image = cv2.imread(sys.argv[1])

T = np.float32([[1, 0, int(sys.argv[2])], [0, 1, int(sys.argv[3])]])

translated = cv2.warpAffine(image, T, (image.shape[1], image.shape[0]))

cv2.imwrite(sys.argv[1], translated)