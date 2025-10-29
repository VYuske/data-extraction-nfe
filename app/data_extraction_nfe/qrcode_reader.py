import cv2
import time
from pyzbar.pyzbar import decode
from .utils.qrcode_reader_utils import *

class QRcodeReader():
    """
    A class for real-time QR code detection and decoding using OpenCV and Pyzbar.

    This class provides an interface to access a webcam, capture frames, detect QR codes,
    and extract their data (URL, type, and bounding box). It can be used in real-time
    applications that need to process QR codes from a live camera feed.

    Attributes
    ----------
    capture : cv2.VideoCapture
        OpenCV video capture object for the specified camera index.
    delay : float
        Delay (in seconds) between frame captures to control processing rate.

    Methods
    -------
    get_frame(get_detection=True)
        Captures a frame from the webcam, decodes any QR codes found, and returns
        both the frame and detection data (URL, type, bbox, detected flag).

    release()
        Releases the webcam resource and closes the camera stream.

    Example
    -------
    >>> reader = QRcodeReader(camera_index=0, delay=0.01)
    >>> while True:
    ...     data = reader.get_frame()
    ...     if data['detected']:
    ...         print(f"QR Code Detected: {data['url']}")
    ...     # Press 'q' in your main loop to exit, then release:
    >>> reader.release()

    Dependencies
    ------------
    - OpenCV (cv2)
    - Pyzbar
    - NumPy
    - utils.qrcode_reader_utils (polygon_to_bbox, extract_detection_data)
    """

    def __init__(self, delay=10e-3, camera_index=0):
        # Create a QRCodeDetector object

        self.capture = cv2.VideoCapture(index=camera_index)
        self.delay = delay

    def get_frame(self, get_detection=True):
        url = ""
        type = None
        bbox = None
        detected = False

        time.sleep(self.delay)

        # Read a frame from the camera
        ret, frame = self.capture.read()

        # If frame is not read successfully, break the loop
        if not ret:
            raise RuntimeError("Error: Failed to grab frame.")

        # Detect and decode the QR code
        detections = decode(frame)
        
        if len(detections) > 0 and get_detection:
            url, type, bbox = extract_detection_data(detections[0])
            detected = True

        return {
            'frame': frame,
            'url': url,
            'type': type,
            'bbox': bbox,
            'detected': detected
        }

    def release(self):
        self.capture.release()
