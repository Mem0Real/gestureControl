import cv2 as cv
# import matplotlib.pyplot as plt

img = cv.imread('Photos/ppl.jpeg')
img = cv.resize(img, (img.shape[1]-350, img.shape[0]-200))
# img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
# img = cv.resize(img, (img.shape[1]-80, img.shape[0]))
cv.imshow('People', img)

# BGR to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# Show RGB image
# plt.imshow(rgb)
# plt.show()

# All the above can be converted back
# Example GreyScale to BGR

gray2bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('GRAY --> BGR', gray2bgr)

cv.waitKey(0)
