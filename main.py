import cv2
import time

# Create a QRCodeDetector object
detector = cv2.QRCodeDetector()
cap = cv2.VideoCapture(0)

while True:
    time.sleep(10e-3)

    # Read a frame from the camera
    ret, frame = cap.read()

    # If frame is not read successfully, break the loop
    if not ret:
        print("Failed to grab frame.")
        break

    # Detect and decode the QR code
    data, bbox, rectified_image = detector.detectAndDecode(frame)

    if bbox is not None:
        print(data, bbox)
        print(f"QR Code detected: {data}")

        # Convert bbox_points to integer type and reshape for polylines
        # bbox_points is typically a 3D array (1, 4, 2) representing 4 corners (x, y)
        bbox = bbox.astype(int).reshape((-1, 1, 2))

        # Draw the bounding box using polylines
        # Arguments: image, array of points, is_closed, color, thickness
        cv2.polylines(frame, [bbox], True, (0, 255, 0), 2) # Green color, 2 thickness

        # Optionally, display the decoded data on the image
        cv2.putText(frame, data, (bbox[0][0][0], bbox[0][0][1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        if data:
            cv2.imwrite(data+'.jpg', rectified_image)
        
    # Display the frame
    cv2.imshow('Webcam Feed', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

