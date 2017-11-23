import sys
import cv2

image = cv2.imread(sys.argv[1])

grayscale = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.imwrite(sys.argv[1], grayscale)