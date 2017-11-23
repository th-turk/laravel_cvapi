import sys
import cv2
import numpy as np

image = cv2.imread(sys.argv[1])

B, G, R = cv2.split(image)

zeros = np.zeros((image.shape[0], image.shape[1]), np.uint8)

green_image = cv2.merge([zeros, G, zeros])

cv2.imwrite(sys.argv[1], green_image)