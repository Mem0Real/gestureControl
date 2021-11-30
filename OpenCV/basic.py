import cv2 as cv

img = cv.imread('Photos/dog.jpeg')
cv.imshow('Man\'s best friend', img)

# Convert image to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', gray)

# Blur an image
blur = cv.blur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blurred', blur)

# Edge Cascade
canny = cv.Canny(img, 1, 575)
cv.imshow('Canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# Resizing
resize = cv.resize(img, (img.shape[1]*2, img.shape[0]*2), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Image', resize)

# Cropping
cropped = img[50:400, 50:600]
cv.imshow('Cropped Image', cropped)

cv.waitKey(0)