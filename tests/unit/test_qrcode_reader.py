import pytest
import numpy as np
from unittest.mock import patch, MagicMock
from libs.data_extraction_nfe.qrcode_reader import QRcodeReader

@pytest.fixture
def mock_frame():
    # Create a dummy frame (e.g., 480x640 black image)
    return np.zeros((480, 640, 3), dtype=np.uint8)

@pytest.fixture
def reader():
    # Instantiate without actually opening a webcam
    with patch("cv2.VideoCapture") as mock_capture:
        mock_instance = MagicMock()
        mock_capture.return_value = mock_instance
        return QRcodeReader(delay=0.0, camera_index=0)


def test_init_creates_capture_object():
    with patch("cv2.VideoCapture") as mock_capture:
        reader = QRcodeReader()
        mock_capture.assert_called_once_with(index=0)
        assert reader.delay == pytest.approx(0.01, 1e-3)


def test_get_frame_no_detection(reader, mock_frame):
    """Test get_frame() when no QR codes are detected."""
    # Mock camera.read() to return a valid frame
    reader.capture.read.return_value = (True, mock_frame)

    # Mock pyzbar.decode to return no detections
    with patch("data_extraction_nfe.qrcode_reader.decode", return_value=[]):
        result = reader.get_frame()

    assert isinstance(result["frame"], np.ndarray)
    assert result["detected"] is False
    assert result["url"] == ""
    assert result["bbox"] is None
    assert result["type"] is None


def test_get_frame_with_detection(reader, mock_frame):
    """Test get_frame() when a QR code is detected."""
    reader.capture.read.return_value = (True, mock_frame)

    fake_detection = MagicMock()
    fake_url = "https://example.com"
    fake_type = "QRCODE"
    fake_bbox = [100, 200, 300, 400]

    # Patch both decode and extract_detection_data
    with patch("data_extraction_nfe.qrcode_reader.decode", return_value=[fake_detection]), \
         patch("data_extraction_nfe.qrcode_reader.extract_detection_data",
               return_value=(fake_url, fake_type, fake_bbox)):

        result = reader.get_frame()

    assert result["detected"] is True
    assert result["url"] == fake_url
    assert result["type"] == fake_type
    assert result["bbox"] == fake_bbox


def test_get_frame_failure_to_grab_frame(reader):
    """Test when the camera fails to return a frame."""
    reader.capture.read.return_value = (False, None)

    with pytest.raises(RuntimeError, match="Failed to grab frame"):
        reader.get_frame()


def test_release(reader):
    """Ensure the camera resource is released."""
    reader.release()
    reader.capture.release.assert_called_once()
