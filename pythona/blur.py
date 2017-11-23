import sys
import numpy as np
import cv2


image = cv2.imread(sys.argv[1])

kernel_blur = np.ones((int(sys.argv[2]), int(sys.argv[2])), np.float32) / (int(sys.argv[2]) * int(sys.argv[2]))


new_image = cv2.filter2D(image, -1, kernel_blur)
cv2.imwrite(sys.argv[1], new_image)