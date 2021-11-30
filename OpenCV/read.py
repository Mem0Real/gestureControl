import cv2 as cv
import numpy as np

# img = cv.imread('Photos/cat.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0)

# Reading videos

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

# Show Edged video
    # canny = cv.Canny(frame, 125, 175)
    # cv.imshow('Canny', canny)

# Show Threshold video And it's canny
    # Resize Frame
#     frame = cv.flip(frame, 1)
#     frame = frame[0:frame.shape[0], frame.shape[1]//2-frame.shape[1]//4:frame.shape[1]//2+frame.shape[1]//4]
#     blank = np.zeros(frame.shape, dtype='uint8')
#
#     grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#
#     ret, thresh = cv.threshold(grey, 50, 195, cv.THRESH_BINARY)
#     cv.imshow('Threshold', thresh)
#
#     canny = cv.Canny(thresh, 125, 175)
#     cv.imshow('Canny', canny)
#
#     contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#
#     cv.drawContours(blank, contours, -1, (0, 0, 255), thickness=1)
#     cv.imshow('Contour on Blank', blank)

    cv.imshow('Videos', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()

cv.destroyAllWindows()


