import streamlit as st
from libs.data_extraction_nfe import QRcodeReader
from libs.data_extraction_nfe.utils import draw_detection
import webbrowser

st.set_page_config(page_title="QR Code Reader", layout="centered")

# Initialize session state
if "camera_active" not in st.session_state:
    st.session_state.camera_active = False
if "qrcode_reader" not in st.session_state:
    st.session_state.qrcode_reader = None
if "detected_url" not in st.session_state:
    st.session_state.detected_url = None

# Functions
def start_qrcode_reader():
    st.session_state.qrcode_reader = QRcodeReader()
    st.session_state.camera_active = True
    st.session_state.detected_url = None

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

# Live camera loop
while st.session_state.camera_active:
    frame_dictionary = st.session_state.qrcode_reader.get_frame(get_detection=True)
    frame = frame_dictionary["frame"]

    if frame_dictionary["detected"]:
        frame = draw_detection(frame, frame_dictionary["url"], frame_dictionary["bbox"])
        st.session_state.detected_url = frame_dictionary["url"]
        stop_qrcode_reader()

    frame_placeholder.image(frame, channels="BGR")

# Show detected URL and button
if st.session_state.detected_url:
    st.success("✅ QR Code detected!")
    st.write(f"**URL:** {st.session_state.detected_url}")
    if st.button("🌐 Open Link"):
        webbrowser.open(st.session_state.detected_url, new=2)
