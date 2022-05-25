import cv2
import time

def saveCurr(img):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    cv2.imwrite(f'FilterResult/{timestr}.png', img)