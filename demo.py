import cv2

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Live Camera Feed', frame)

    # Break the loop on 'q' key press 
    # cureant speed is not enuf to play large video that reasun 
    #@Himanshu-up speed of file 1 to 3
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
