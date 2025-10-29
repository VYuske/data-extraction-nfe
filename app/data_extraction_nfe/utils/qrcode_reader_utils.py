import numpy as np
import cv2

def polygon_to_bbox(polygon):
    """
    Converts a polygon object into a NumPy array of (x, y) coordinates.
    
    Parameters
    ----------
    polygon : list
        List of point objects with `x` and `y` attributes.

    Returns
    -------
    np.ndarray
        Array of polygon points as [[x1, y1], [x2, y2], ...].
    """
    bbox = [[p.x, p.y] for p in polygon]
    return np.array(bbox)


def extract_detection_data(detection):
    """
    Extracts relevant information from a QR code detection object.
    
    Parameters
    ----------
    detection : pyzbar.Decoded
        QR code detection result from pyzbar.

    Returns
    -------
    tuple
        (url, type, bbox) where:
        - url (str): Decoded QR code data.
        - type (str): Barcode type (e.g., 'QRCODE').
        - bbox (np.ndarray): Array of bounding box coordinates.
    """
    url = detection.data.decode('utf-8')
    type = detection.type
    bbox = polygon_to_bbox(detection.polygon)
    return url, type, bbox


def draw_detection(frame, url, bbox):
    """
    Draws a bounding box and decoded QR code data on the given frame.

    Parameters
    ----------
    frame : np.ndarray
        Image frame where the detection will be drawn.
    url : str
        Decoded QR code data to display.
    bbox : np.ndarray
        Bounding box points of the detected QR code.

    Returns
    -------
    np.ndarray
        Frame with bounding box and text overlay.
    """
    bbox = bbox.astype(int).reshape((-1, 1, 2))
    cv2.polylines(frame, [bbox], isClosed=True, color=(0, 255, 0), thickness=2)
    cv2.putText(
        frame, url,
        (bbox[0][0][0], bbox[0][0][1] - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (0, 255, 0), 2
    )
    return frame
