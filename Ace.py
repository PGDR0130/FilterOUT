import cv2
from cv2 import bitwise_not
import numpy as np
from hsvfilter import HsvFilter
from Toggle import CreateSlides, Get_toggle_value
from SimpleToggle import SimpleToggle
from cv2SaveImg import saveCurr
import time

img = cv2.imread('test1.jpg', cv2.COLOR_BGR2HSV)
background = img

# Settings
reverse = False
MODE = 'Simple'

# init 
if MODE == 'Triditional':
    CreateSlides()
    hsvValue = HsvFilter() 
elif MODE == 'Simple':
    simpTogg = SimpleToggle()

# loop
while True:
    if MODE == 'Triditional':
        Get_toggle_value(hsvValue)
        lower = np.array([hsvValue.hMin, hsvValue.sMin, hsvValue.vMin])
        upper = np.array([hsvValue.hMax, hsvValue.sMax, hsvValue.vMax])

    elif MODE == 'Simple':
        simpTogg.update()
        lowup = simpTogg.getHSVRangeValue()
        lower = np.array(lowup[0])
        upper = np.array(lowup[1])
        reverse = simpTogg.reverseState
        if simpTogg.saveHandle(toFalse=True):
            saveCurr(result)

    mask = cv2.inRange(img, lower, upper)


    if(not reverse):
        mask = bitwise_not(mask)
    
    result = cv2.bitwise_and(img, background, mask=mask)
        
    # showing result
    cv2.imshow('img', result)
    cv2.imshow('mask', mask)


    # quit program
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

    # limit cpu usage
    time.sleep(0.05)