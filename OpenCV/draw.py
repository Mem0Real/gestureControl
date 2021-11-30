import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('blank', blank)

# 1. Paint image a certain color
blank[10:60, 100:300] = 0, 255, 0
blank[70:120, 100:300] = 255, 0, 0
cv.imshow('Green', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 255), thickness=1)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 60, (0, 255, 0), thickness=1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (blank.shape[1]//2, 10), (blank.shape[1]//2, blank.shape[0]//2), (140, 14, 84), thickness=5)
cv.imshow('Line', blank)

# 5. Draw a text
cv.putText(blank, "How you doin?", (blank.shape[1]//2, 50), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 255), 2)
cv.imshow('Text', blank)
cv.waitKey(0)