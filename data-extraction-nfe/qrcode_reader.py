import cv2
import time
from pyzbar.pyzbar import decode
import numpy as np
from utils.utils import polygon_to_bbox

class QRcodeReader():
    def __init__(self, camera_index, delay=10e-3):
        # Create a QRCodeDetector object
        self.capture = cv2.VideoCapture(index=camera_index)
        self.delay = delay

    def run_webcan(self):
        while True:
            time.sleep(self.delay)

            # Read a frame from the camera
            ret, frame = self.capture.read()

            # If frame is not read successfully, break the loop
            if not ret:
                raise("Error: Failed to grab frame.")

            # Detect and decode the QR code
            detections = decode(frame)

            if len(detections) > 0:
                frame = self.display_detections(detections, frame)

            # Display the frame
            cv2.imshow('Webcam Feed', frame)

            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def get_detections(self):
        while True:
            time.sleep(self.delay)

            # Read a frame from the camera
            ret, frame = self.capture.read()

            # If frame is not read successfully, break the loop
            if not ret:
                raise("Error: Failed to grab frame.")

            # Detect and decode the QR code
            detections = decode(frame)

            cv2.imshow('Webcam Feed', frame)
            
            if len(detections) > 0:
                return detections

    def display_detections(self, detections, frame):

        for detection in detections:
            print(f"QR Code detected: {detections}")

            bbox = polygon_to_bbox(detections[0].polygon)
            bbox = bbox.astype(int).reshape((-1, 1, 2))

            # Draw the bounding box using polylines
            # Arguments: image, array of points, is_closed, color, thickness
            cv2.polylines(frame, [bbox], True, (0, 255, 0), 2) # Green color, 2 thickness

            # Optionally, display the decoded data on the image
            cv2.putText(frame, str(detection.data, encoding='utf-8'), (bbox[0][0][0], bbox[0][0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return frame
