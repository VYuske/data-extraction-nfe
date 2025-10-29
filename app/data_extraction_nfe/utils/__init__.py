"""
Utility package for shared helper functions.

Modules included:
- draw_utils: Drawing and visualization helpers (OpenCV, etc.)
- image_utils: Image processing utilities
- file_utils: File and path management functions
"""

from .qrcode_reader_utils import (
    polygon_to_bbox,
    extract_detection_data,
    draw_detection,
)

__all__ = [
    "polygon_to_bbox",
    "extract_detection_data",
    "draw_detection",
]