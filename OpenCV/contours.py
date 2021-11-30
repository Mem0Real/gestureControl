import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
img = cv.resize(img, (img.shape[1]//4, img.shape[0]//4), interpolation=cv.INTER_CUBIC)
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)


# First we change the image to greyscale

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Greyed', grey)

# Blur the image first to decrease contour count

blur = cv.blur(grey, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Next we grab the canny

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# One way to find contours involves

ret, thresh = cv.threshold(grey, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)


# Now to find the contours

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

# Draw contours on another image

cv.drawContours(blank, contours, -1, (0, 0, 255), thickness=1)
cv.imshow('Contour on Blank', blank)




cv.waitKey(0)
