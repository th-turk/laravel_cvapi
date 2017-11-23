import sys
import cv2
import numpy as np

image = cv2.imread(sys.argv[1])

B, G, R = cv2.split(image)

zeros = np.zeros((image.shape[0], image.shape[1]), np.uint8)

blue_image = cv2.merge([B, zeros, zeros])

cv2.imwrite(sys.argv[1], blue_image)