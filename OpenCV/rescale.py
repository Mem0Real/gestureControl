import cv2 as cv


def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# # Reading Images
# img = cv.imread('Photos/dog.jpeg')
# img = rescale_frame(img)
# cv.imshow('Image', img)

# Reading videos
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame)
    cv.imshow('Videos', frame)
    cv.imshow('Resized Video', frame_resized)
    cv.imshow('More Resized Video', rescale_frame(frame, scale=0.4))

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()

cv.destroyAllWindows()
