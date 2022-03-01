import cv2
import time
from scipy.spatial import distance


# Load the Haar cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Function to calculate the eye aspect ratio
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Threshold for detecting a blink
EAR_THRESHOLD = 0.3

# Initialize variables
blink_counter = 0
sleepy_message_shown = False
start_time = time.time()

# Open the webcam
cap = cv2.VideoCapture("C:\\Users\\M.Manish kumar\\OneDrive\\Pictures\\Camera Roll\\WIN_20231113_07_35_17_Pro.mp4")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes in the face region
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            eye = roi_gray[ey:ey + eh, ex:ex + ew]
            eye_aspect_ratio_value = eye_aspect_ratio([(ex, ey), (ex + ew // 2, ey), (ex + ew, ey), (ex, ey + eh // 2), (ex + ew // 2, ey + eh // 2), (ex + ew, ey + eh // 2)])
            
            # Check if the person is closing their eyes
            if eye_aspect_ratio_value < EAR_THRESHOLD:
                blink_counter += 1
            else:
                blink_counter = 0
                sleepy_message_shown = False

            # Check if the person has closed their eyes for more than 5 seconds
            if blink_counter >= 5 and not sleepy_message_shown:
                sleepy_message_shown = True
                print("Sleepy! You've closed your eyes for more than 5 seconds.")

            # Draw rectangles around the eyes
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
