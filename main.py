import cv2

cap = cv2.VideoCapture(0)  # Initialize the camera

while True:
    ret, frame = cap.read()  # Capture frame-by-frame
    if ret:
        # Process frame here (e.g., apply image recognition)
        cv2.imshow('Frame', frame)  # Display the resulting frame

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit condition
            break

cap.release()  # When everything is done, release the capture
cv2.destroyAllWindows()
