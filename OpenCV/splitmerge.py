import cv2 as cv
import numpy as np

img = cv.imread('Photos/aut1.jpg')
img = cv.resize(img, (img.shape[1]//4, img.shape[0]//4))
cv.imshow('Autumn', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Im Blue', blue)
cv.imshow('Im Green', green)
cv.imshow('Im Red', red)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)
cv.waitKey(0)
