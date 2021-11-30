import cv2 as cv
import numpy as np

img = cv.imread('Photos/dog.jpg')
cv.imshow('Dog', img)

# Translation


def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensions)

# When calling translate function,
# x --> Shift to the Right
# -x --> Shift to the Left
# y --> Shift Down
# -y --> Shift Up


translated = translate(img, 0, -60)
cv.imshow('Translated', translated)

# Rotation


def rotate(img, angle, rot_point=None):
    (height, width) = img.shape[:2]

    if rot_point is None:
        rot_point = (width//2, height//2)

    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rot_mat, dimensions)


rotated = rotate(img, -45, rot_point=(100, 5))
cv.imshow('Rotated', rotated)

# Flipping
flip = cv.flip(img, 1)
cv.imshow('Flipped', flip)


cv.waitKey(0)
