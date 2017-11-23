import sys
import cv2
import numpy as np

image = cv2.imread(sys.argv[1])

type_of_interpolation = int(sys.argv[4])

if type_of_interpolation == 0:
	img_scaled = cv2.resize(image, (int(sys.argv[2]), int(sys.argv[3])), interpolation = cv2.INTER_NEAREST)
elif type_of_interpolation == 1:
	img_scaled = cv2.resize(image, (int(sys.argv[2]), int(sys.argv[3])), interpolation = cv2.INTER_AREA)
elif type_of_interpolation == 2:
	img_scaled = cv2.resize(image, (int(sys.argv[2]), int(sys.argv[3])), interpolation = cv2.INTER_LINEAR)
elif type_of_interpolation == 3:
	img_scaled = cv2.resize(image, (int(sys.argv[2]), int(sys.argv[3])), interpolation = cv2.INTER_CUBIC)
else:
	img_scaled = cv2.resize(image, (int(sys.argv[2]), int(sys.argv[3])), interpolation = cv2.INTER_LANCZOS4)

cv2.imwrite(sys.argv[1], img_scaled)