from cv2 import bitwise_not
import numpy as np
import cv2 as cv
from hsvfilter import HsvFilter
from Toggle import CreateSlides, Get_toggle_value

img = cv.imread('test1.jpg', cv.COLOR_BGR2HSV)
reverse = True

CreateSlides()
hsvValue = HsvFilter() 


while True:
    Get_toggle_value(hsvValue)
    lower = np.array([hsvValue.hMin, hsvValue.sMin, hsvValue.vMin])
    upper = np.array([hsvValue.hMax, hsvValue.sMax, hsvValue.vMax])

    mask = cv.inRange(img, lower, upper)


    if(hsvValue.invert == 0):
        result = cv.bitwise_and(img, img, mask=mask)
    else:
        mask = bitwise_not(mask)
        result = cv.bitwise_and(img, img, mask=mask)

    # showing result
    cv.imshow('img', result)
    cv.imshow('mask', mask)


    # quit program
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break