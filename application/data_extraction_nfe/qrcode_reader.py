import cv2
import time
from pyzbar.pyzbar import decode
from .utils.utils import polygon_to_bbox, detection_array_to_dictionary

class QRcodeReader():
    """
        QRcodeReader
        ============

        This class provides a simple interface for capturing video from a webcam, detecting, and decoding QR Codes in real time using OpenCV and pyzbar.

        Main methods:
        -------------
        - __init__(camera_index, delay): Initializes webcam capture at the specified index. The 'delay' parameter controls the interval between frames.
        - run_webcan(get_detections=True): Starts the webcam capture loop, detects QR Codes, and displays the video in real time. Shows a message in the lower left corner instructing to press 'q' to exit. Returns detections if found.
        - display_detections(detections, frame): Draws the bounding box of detected QR Codes and displays the decoded content on the video.
        - __del__(): Releases webcam resources and closes OpenCV windows when the object is destroyed.

        Usage:
        ------
        Create an instance of the class with the webcam index and call the run_webcan() method to start reading QR Codes.

        Example:
        --------
        reader = QRcodeReader(camera_index=0)
        reader.run_webcan()

        Dependencies:
        -------------
        - OpenCV (cv2)
        - pyzbar
        - utils.utils.polygon_to_bbox

    """

    def __init__(self, delay=10e-3, camera_index=0):
        # Create a QRCodeDetector object

        self.capture = cv2.VideoCapture(index=camera_index)
        self.delay = delay

    def get_frame(self, get_detection=True):
        time.sleep(self.delay)

        # Read a frame from the camera
        ret, frame = self.capture.read()

        # If frame is not read successfully, break the loop
        if not ret:
            raise RuntimeError("Error: Failed to grab frame.")

        # Detect and decode the QR code
        detections = decode(frame)
        
        if len(detections) > 0 and get_detection == True:
            return {
                'frame': frame,
                'detection': detection_array_to_dictionary(detections[0])
            }

        return {
            'frame': frame,
            'detection': None
        }

    def draw_detection(self, detection, frame):
        bbox = detection['bbox']
        url = detection['url']
        bbox = bbox.astype(int).reshape((-1, 1, 2))

        # Draw the bounding box using polylines
        # Arguments: image, array of points, is_closed, color, thickness
        cv2.polylines(frame, [bbox], True, (0, 255, 0), 2) # Green color, 2 thickness

        # Optionally, display the decoded data on the image
        cv2.putText(frame, url, (bbox[0][0][0], bbox[0][0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return frame

    def release(self):
        self.capture.release()
