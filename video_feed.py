import cv2

capture = cv2.VideoCapture("https://www.youtube.com/watch?v=5qap5aO4i9A")

while(True):
    _, frame = capture.read()
    cv2.imshow('livestream', frame)

    if cv2.waitKey(1) == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()