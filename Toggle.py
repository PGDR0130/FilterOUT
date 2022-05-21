import cv2 as cv
from hsvfilter import HsvFilter


def save():
    pass

def CreateSlides():
    TRACKBAR_WINDOW = 'slides'

    cv.namedWindow(TRACKBAR_WINDOW, cv.WINDOW_NORMAL)
    cv.resizeWindow(TRACKBAR_WINDOW, 350, 500)

    # required callback. we'll be using getTrackbarPos() to do lookups
    # instead of using the callback.
    def nothing(position):
        pass

    # create trackbars for bracketing.
    # OpenCV scale for HSV is H: 0-179, S: 0-255, V: 0-255
    cv.createTrackbar('HMin',TRACKBAR_WINDOW, 0, 179, nothing)
    cv.createTrackbar('SMin',TRACKBAR_WINDOW, 0, 255, nothing)
    cv.createTrackbar('VMin',TRACKBAR_WINDOW, 0, 255, nothing)
    cv.createTrackbar('HMax',TRACKBAR_WINDOW, 0, 179, nothing)
    cv.createTrackbar('SMax',TRACKBAR_WINDOW, 0, 255, nothing)
    cv.createTrackbar('VMax',TRACKBAR_WINDOW, 0, 255, nothing)
    # Set default value for Max HSV trackbars
    cv.setTrackbarPos('HMax',TRACKBAR_WINDOW, 179)
    cv.setTrackbarPos('SMax',TRACKBAR_WINDOW, 255)
    cv.setTrackbarPos('VMax',TRACKBAR_WINDOW, 255)

    # trackbars for increasing/decreasing saturation and value
    cv.createTrackbar('SAdd',TRACKBAR_WINDOW, 0, 255, nothing)
    cv.createTrackbar('SSub',TRACKBAR_WINDOW, 0, 255, nothing)
    cv.createTrackbar('VAdd',TRACKBAR_WINDOW, 0, 255, nothing)
    cv.createTrackbar('VSub',TRACKBAR_WINDOW, 0, 255, nothing)

    # invert mask
    cv.createTrackbar('Invert',TRACKBAR_WINDOW, 0, 1, nothing)

def Get_toggle_value(hsvValue):
    TRACKBAR_WINDOW = 'slides'
    # Get current positions of all trackbars
    hsv_filter = hsvValue
    hsv_filter.hMin = cv.getTrackbarPos('HMin', TRACKBAR_WINDOW)
    hsv_filter.sMin = cv.getTrackbarPos('SMin', TRACKBAR_WINDOW)
    hsv_filter.vMin = cv.getTrackbarPos('VMin', TRACKBAR_WINDOW)
    hsv_filter.hMax = cv.getTrackbarPos('HMax', TRACKBAR_WINDOW)
    hsv_filter.sMax = cv.getTrackbarPos('SMax', TRACKBAR_WINDOW)
    hsv_filter.vMax = cv.getTrackbarPos('VMax', TRACKBAR_WINDOW)
    hsv_filter.sAdd = cv.getTrackbarPos('SAdd', TRACKBAR_WINDOW)
    hsv_filter.sSub = cv.getTrackbarPos('SSub', TRACKBAR_WINDOW)
    hsv_filter.vAdd = cv.getTrackbarPos('VAdd', TRACKBAR_WINDOW)
    hsv_filter.vSub = cv.getTrackbarPos('VSub', TRACKBAR_WINDOW)
    hsv_filter.invert= cv.getTrackbarPos('Invert', TRACKBAR_WINDOW)