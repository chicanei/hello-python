import cv2 as cv

#img = cv.imread('Photos/cat_large2.jpg')
#cv.imshow('Cat', img)

def resacleFrame(frame, scale = 0.75):
    width = int(frame. shape[1]* scale)
    height = int(frame. shape[0]* scale)
    dimensions = (width, height)

    return cv. resize (frame, dimensions, interpolation = cv.INTER_AREA)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = resacleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized )

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()