import cv2 as cv

cap = cv.VideoCapture(0)  # Initialize the camera

while True:
    ret, frame = cap.read()  # Capture frame-by-frame
    if ret:
        # Process frame here (e.g., apply image recognition)
        cv.imshow('Frame', frame)  # Display the resulting frame

        if cv.waitKey(1) & 0xFF == ord('q'):  # Exit condition
            break

cap.release()  # When everything is done, release the capture
cv.destroyAllWindows()
