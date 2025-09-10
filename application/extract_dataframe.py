import pandas as pd
import streamlit as st

text_input = st.text_input("Enter the text from the web page:", key="text_input")
st.write(text_input)