import sys
import cv2

image = cv2.imread(sys.argv[1])

counter = int(sys.argv[2])

for x in xrange(0, counter):
	image = cv2.pyrDown(image)

cv2.imwrite(sys.argv[1], image)