import cv2
import numpy as np

# Thresholds for mouth aspect ratio and consecutive frames
MOUTH_ASPECT_RATIO_THRESHOLD = 0.5
CONSECUTIVE_FRAMES_THRESHOLD = 20

# Initialize variables
frame_count = 0
consecutive_frames = 0

# Open the video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use a face cascade classifier (you may need to adjust the path)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Extract the region of interest (ROI) around the detected face
        roi_gray = gray[y:y + h, x:x + w]

        # Use a mouth cascade classifier (you may need to adjust the path)
        mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mouth.xml')
        mouths = mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)

        for (mx, my, mw, mh) in mouths:
            # Calculate the mouth aspect ratio
            mouth_aspect_ratio = float(mw) / mh

            # Check if the mouth aspect ratio is below the threshold
            if mouth_aspect_ratio < MOUTH_ASPECT_RATIO_THRESHOLD:
                consecutive_frames += 1
            else:
                consecutive_frames = 0

            # If drowsiness is detected for consecutive frames, trigger an alert
            if consecutive_frames >= CONSECUTIVE_FRAMES_THRESHOLD:
                cv2.putText(frame, "Drowsiness Detected!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow("Drowsiness Detection", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
