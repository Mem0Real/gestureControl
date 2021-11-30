import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (3, 3))
cv.imshow('Img Blur', average)

# Gaussian Blur
gb = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gb)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 15, 40, 55)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
