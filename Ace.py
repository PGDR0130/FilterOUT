from cv2 import bitwise_not
import numpy as np
import cv2
from hsvfilter import HsvFilter
from Toggle import CreateSlides, Get_toggle_value

img = cv2.imread('test1.jpg', cv2.COLOR_BGR2HSV)
reverse = True

CreateSlides()
hsvValue = HsvFilter() 


while True:
    Get_toggle_value(hsvValue)
    lower = np.array([hsvValue.hMin, hsvValue.sMin, hsvValue.vMin])
    upper = np.array([hsvValue.hMax, hsvValue.sMax, hsvValue.vMax])

    mask = cv2.inRange(img, lower, upper)


    if(hsvValue.invert == 0):
        result = cv2.bitwise_and(img, img, mask=mask)
    else:
        mask = bitwise_not(mask)
        result = cv2.bitwise_and(img, img, mask=mask)

    # showing result
    cv2.imshow('img', result)
    cv2.imshow('mask', mask)


    # quit program
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break