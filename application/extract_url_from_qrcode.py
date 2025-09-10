import streamlit as st
from data_extraction_nfe import QRcodeReader
import webbrowser


st.title("EXtract URL from QR Code")
reader = QRcodeReader()
url = 'No URL detected yet'

camera_toggle = st.toggle("Activate Camera", value=False)

frame_placeholder = st.empty()

while reader.capture.isOpened() and camera_toggle:
    frame_dictionary = reader.get_frame(get_detection=True)
    frame = frame_dictionary['frame']
    frame_placeholder.image(frame, channels="BGR")

    if frame_dictionary['detection'] is not None:
        detection = frame_dictionary['detection']
        frame = reader.draw_detection(detection, frame)
        frame_placeholder.image(frame, channels="BGR")
        webbrowser.open(url=detection['url'], new=2)
        break
