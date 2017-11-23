import sys
import numpy as np
import cv2


image = cv2.imread(sys.argv[1])

kernel_sharpening = np.array([
	[-1, -1, -1],
	[-1, 9, -1],
	[-1, -1, -1]
])


new_image = cv2.filter2D(image, -1, kernel_sharpening)
cv2.imwrite(sys.argv[1], new_image)