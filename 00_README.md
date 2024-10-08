# Bottle-Detection-YOLOv8
A YOLOv8 custom-trained bottle detection system using webcam
Bottle Detection Using YOLOv8 Custom-Trained Model

This project demonstrates a custom-trained YOLOv8 model for detecting bottles using a webcam. The model was trained using a dataset from Roboflow and can run in real-time on your local machine. The training process was done on Google Colab, while detection is handled via a Python script that uses your webcam on macOS.

Features

YOLOv8 Custom Training: A custom YOLOv8 model specifically trained to detect bottles.
Webcam Integration: Real-time detection using your local webcam.
Python Implementation: Fully implemented in Python, ensuring ease of customization.
Requirements

To run this project, you'll need the following dependencies:

Python 3.x
Ultralytics YOLOv8
OpenCV (for webcam access and image handling)
Torch (for YOLOv8 inference)
Roboflow (optional for dataset management)
The 01_yolov8_training.py (https://github.com/Tajbir09/Bottle-Detection-YOLOv8/edit/main/00_README.md#:~:text=01_yolov8_training.py) file includes python code for training YOLOv8 on custom data set.
The 02_yolo_detection.py (https://github.com/Tajbir09/Bottle-Detection-YOLOv8/edit/main/00_README.md#:~:text=01_yolov8_training.py-,02_yolo_detection.py,-Editing%2000_README.md) file includes python code to run the trained model on local device using webcam for live detection.
