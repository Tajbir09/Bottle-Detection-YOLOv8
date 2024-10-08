# Import required libraries
from ultralytics import YOLO
import cv2

# Load the trained YOLOv8 model
model = YOLO('/Users/tajbir/Downloads/best.pt') #Define the path to the (best.pt) file. 
cap = cv2.VideoCapture(0)  # 0 is the default webcam

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    
    if not ret:
        print("Error: Could not read frame")
        break

    # Use the model to detect objects in the frame
    results = model(frame)

    # Plot the detection results on the frame
    annotated_frame = results[0].plot()

    # Show the frame with the detected objects
    cv2.imshow("YOLOv8 Webcam Detection", annotated_frame)

    # Press 'q' to quit the video stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
