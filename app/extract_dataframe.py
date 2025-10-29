import pandas as pd
import streamlit as st
from data_extraction_nfe import TextParser

st.title("Extract DataFrame from Text")
text_parser = TextParser()

text_input = st.text_input("Enter the text from the web page:", key="text_input")

data = pd.DataFrame(text_parser.parse_text(text_input))
st.write(data)