import streamlit as st
from data_extraction_nfe import QRcodeReader
import webbrowser

# Initialize session state
if "camera_active" not in st.session_state:
    st.session_state.camera_active = False
if "qrcode_reader" not in st.session_state:
    st.session_state.qrcode_reader = None

# Function to start the webcam
def start_qrcode_reader():
    st.session_state.qrcode_reader = QRcodeReader()
    st.session_state.camera_active = True

# Function to stop the webcam
def stop_qrcode_reader():
    if st.session_state.qrcode_reader is not None:
        st.session_state.qrcode_reader.release()
    st.session_state.camera_active = False

# Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("▶️ Start Camera"):
        start_qrcode_reader()
with col2:
    if st.button("⏹ Stop Camera"):
        stop_qrcode_reader()

st.title("Extract URL from QR Code")

frame_placeholder = st.empty()

while st.session_state.camera_active:
    frame_dictionary = st.session_state.qrcode_reader.get_frame(get_detection=True)
    frame = frame_dictionary['frame']
    frame_placeholder.image(frame, channels="BGR")

    if frame_dictionary['detection'] is not None:
        detection = frame_dictionary['detection']
        frame = st.session_state.qrcode_reader.draw_detection(detection, frame)
        frame_placeholder.image(frame, channels="BGR")
        webbrowser.open(url=detection['url'], new=2)
        stop_qrcode_reader()
