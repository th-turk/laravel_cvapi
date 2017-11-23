import sys
import numpy as np
import cv2


image = cv2.imread(sys.argv[1])

brightness = np.ones(image.shape, dtype='uint8') * int(sys.argv[2])

new_image = cv2.add(image, brightness)
cv2.imwrite(sys.argv[1], new_image)