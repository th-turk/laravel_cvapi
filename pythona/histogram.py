import cv2
import sys
import numpy as np 
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


image = cv2.imread(sys.argv[1])

blue_channel = cv2.calcHist([image], [0], None, [int(sys.argv[2])], [int(sys.argv[3]), int(sys.argv[4])])
green_channel = cv2.calcHist([image], [1], None, [int(sys.argv[2])], [int(sys.argv[3]), int(sys.argv[4])])
red_channel = cv2.calcHist([image], [2], None, [int(sys.argv[2])], [int(sys.argv[3]), int(sys.argv[4])])

plt.plot(blue_channel, color='blue')
plt.plot(green_channel, color='green')
plt.plot(red_channel, color='red')
plt.savefig(sys.argv[1])