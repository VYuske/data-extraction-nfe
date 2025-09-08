import streamlit as st
from data_extraction_nfe import QRcodeReader

if st.button("Start QR Code Scanner"):
    reader = QRcodeReader(camera_index=0)
    detections = reader.run_webcan(get_detections=True)
    
    st.write(detections)
    
    if detections is not None:
        st.link_button("Go to URL", detections['url'])