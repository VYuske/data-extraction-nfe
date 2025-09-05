from qrcode_reader import QRcodeReader
from bs4 import BeautifulSoup

reader = QRcodeReader(camera_index=0)
reader.run_webcan()
# detections = reader.run_webcan()
# print(detections)