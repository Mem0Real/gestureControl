import cv2 as cv

# Show images
#
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)

# Show webcam

video = cv.VideoCapture(0)

while True:
    isTrue, frame = video.read()
    cv.imshow('Me', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()
