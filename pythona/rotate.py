import sys
import cv2
import numpy as np

image = cv2.imread(sys.argv[1])

height, width = image.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((int(sys.argv[2]),int(sys.argv[3])), int(sys.argv[4]), 1)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imwrite(sys.argv[1], rotated_image)