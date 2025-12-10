import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

def default_page():
    st.write("This is the default page. Please select a page from the sidebar.")

def main():
    # Set the app title
    st.title("Gestão de NF-e com Streamlit")

    pages = [
        st.Page(default_page, title="Home"),
        st.Page("pages/extract_url_from_qrcode.py", title="Extract URL from QR Code"),
        st.Page("pages/extract_dataframe.py", title="Extract DataFrame"),
    ]

    pg = st.navigation(pages)
    pg.run()
        
if __name__ == "__main__":
    main()