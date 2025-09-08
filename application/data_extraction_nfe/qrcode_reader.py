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

    def __init__(self, camera_index, delay=10e-3):
        # Create a QRCodeDetector object
        self.capture = cv2.VideoCapture(index=camera_index)
        self.delay = delay

    def run_webcan(self, get_detections=True):

        while True:
            time.sleep(self.delay)

            # Read a frame from the camera
            ret, frame = self.capture.read()

            # If frame is not read successfully, break the loop
            if not ret:
                raise RuntimeError("Error: Failed to grab frame.")

            # Detect and decode the QR code
            detections = decode(frame)
            
            cv2.putText(frame, "Pressione 'q' para sair",  (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            if len(detections) > 0:
                frame = self.display_detections(detections, frame)

            # Display the frame
            cv2.imshow('Webcam Feed', frame)
            
            if len(detections) > 0 and get_detections == True:
                self.capture.release()
                cv2.destroyAllWindows()
                return detection_array_to_dictionary(detections[0])
            
            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.capture.release()
                cv2.destroyAllWindows()
                break

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

    def __del__(self):
        if hasattr(self, 'capture') and self.capture.isOpened():
            self.capture.release()
        cv2.destroyAllWindows()
