import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('circle', circle)

# Bitwise AND --> Intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise and', bitwise_and)

# Bitwise OR --> Both intersecting and non-intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise Or', bitwise_or)

# Bitwise XOR --> Non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# Bitwise NOT --> Inverts the biniary color
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Rectangle Not', bitwise_not)

cv.waitKey(0)