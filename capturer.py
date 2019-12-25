import cv2


def capture(count):
    cap = cv2.VideoCapture(0)
    returnable = []
    for i in range(count):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        yield gray