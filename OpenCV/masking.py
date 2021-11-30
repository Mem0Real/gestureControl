import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Black', blank)

rectangle_mask = cv.rectangle(blank.copy(), (0, 0), (img.shape[1]//2 + 90, img.shape[0]//2 + 70), 255, -1)
circle_mask = cv.circle(blank.copy(), (img.shape[1]//2 + 195, img.shape[0]//2 - 70), 100, 255, -1)
weird_mask = cv.bitwise_and(circle_mask, rectangle_mask)


cv.imshow('Square Mask', rectangle_mask)
cv.imshow('Circle Mask', circle_mask)
cv.imshow('Weird Mask', weird_mask)

rectangle_masked = cv.bitwise_and(img, img, mask=rectangle_mask)
circle_masked = cv.bitwise_and(img, img, mask=circle_mask)
weird_masked = cv.bitwise_or(img, img, mask=weird_mask)

cv.imshow('Rectangular Masked image', rectangle_masked)
cv.imshow('Circular Masked image', circle_masked)
cv.imshow('Weird Masked image', weird_masked)

cv.waitKey(0)
