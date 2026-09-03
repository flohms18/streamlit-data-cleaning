import streamlit as st
import pandas as pd

MyDf = pd.DataFrame({
    'First column' : [1,2,3,4],
    'Second column': [10, 20, 30,40]
})

uploaded_file = st.file_uploader("Upload a CSV file")
if uploaded_file is not None : 
    uploaded_csv = pd.read_csv(uploaded_file)
    st.write(uploaded_csv)