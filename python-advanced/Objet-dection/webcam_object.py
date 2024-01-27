from ultralytics import YOLO
import cv2
import cvzone
import math 

cap = cv2.VideoCapture(0)
cap.set(3, 668)
cap.set(4, 480)

model = YOLO("yolov8n.pt")

# Retrieve class names from the model
class_names = model.names

while True:
    success, img = cap.read()
    result = model(img, stream=True)
    
    for r in result:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Calculate width and height of the bounding box
            w, h = x2 - x1, y2 - y1
            
            # Draw rectangle around detected object
            cvzone.cornerRect(img, (x1, y1, w, h))
            
            # Get confidence score
            conf = math.ceil((box.conf[0] * 100)) / 100
            
            # Get class index
            class_id = int(box.cls[0])
            
            # Get class name
            class_name = class_names[class_id]
            
            # Print confidence and class name
            print(f"Class: {class_name}, Confidence: {conf}")

            # Put text on image
            cvzone.putTextRect(img, f"{class_name} {conf}", (x1, y1 - 20))

    cv2.imshow("Image", img)
    cv2.waitKey(1)
