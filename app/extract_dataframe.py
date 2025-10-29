import pandas as pd
import streamlit as st
from data_extraction_nfe import TextParser

# Initialize session state
if "text_parser" not in st.session_state:
    st.session_state.text_parser = TextParser()


st.title("Extract DataFrame from Text")

text_input = st.text_input("Enter the list of items:", key="parse_list_of_items")

data = pd.DataFrame(st.session_state.text_parser.parse_list_of_items(text_input))
st.write(data)

text_input = st.text_input("Enter the details of the nfe:", key="text_input")
text_input = st.session_state.text_parser.parse_nfe_data(text_input)
st.write(text_input)