from matplotlib.pyplot import hsv
import numpy as np
import cv2 as cv
from hsvfilter import HsvFilter
from Toggle import CreateSlides, Get_toggle_value

img = cv.imread('test1.jpg', cv.COLOR_BGR2HSV)

CreateSlides()
hsvValue = HsvFilter() 
while True:
    Get_toggle_value(hsvValue)
    lower = np.array([hsvValue.hMin, hsvValue.sMin, hsvValue.vMin])
    upper = np.array([hsvValue.hMax, hsvValue.sMax, hsvValue.vMax])

    mask = cv.inRange(img, lower, upper)
    result = cv.bitwise_and(img, img, mask=mask)

    cv.imshow('img', result)
    cv.imshow('mask', mask)

    cv.waitKey(1)



# lower = np.array([140, 80, 170])
# upper = np.array([170, 255, 255])

# mask = cv2.inRange(img, lower, upper)

# result = cv2.bitwise_and(img, img, mask=mask)

# cv2.imshow('img', result)
# cv2.imshow('mask', mask)
# cv2.waitKey(0)

# cv2.destroyAllWindows()