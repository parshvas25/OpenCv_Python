#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:22:28 2019

@author: parshvashah
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

BGRImage = cv2.imread('turtle.jpg')
#plt.imshow(BGRImage)
RGBImage = cv2.cvtColor(BGRImage, cv2.COLOR_BGR2RGB)
#plt.imshow(RGBImage)

hsv_frame = cv2.cvtColor(RGBImage, cv2.COLOR_BGR2HSV)
#HSV Color Converstion
low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])
mask = cv2.inRange(hsv_frame,low_green, high_green)
cv2.imshow("Detection", mask )
cv2.waitKey(0)
cv2.destroyAllWindows()
