import streamlit as st

def default_page():
    st.write("This is the default page. Please select a page from the sidebar.")

def main():
    # Set the app title
    st.title("My First Streamlit App")

    # Add some text
    st.write("Welcome to your interactive Streamlit application!")

    pages = [
        st.Page(default_page, title="Home"),
        st.Page("extract_url_from_qrcode.py", title="Extract URL from QR Code"),
        st.Page("extract_dataframe.py", title="Extract DataFrame"),
    ]

    pg = st.navigation(pages)
    pg.run()
        
if __name__ == "__main__":
    main()