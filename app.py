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
    agree = st.checkbox("Remove Duplicates?")
    if agree:
        new_uploaded_csv = uploaded_csv.drop_duplicates()
        new_uploaded_csv_no = new_uploaded_csv.dropna()
        st.write(new_uploaded_csv_no)
        csv = new_uploaded_csv_no.to_csv(index=False).encode("utf-8")

        st.download_button (
            label="Download Clean CSV File",
            data=csv,
            file_name="data.csv",
            mime="text/csv",
            icon=":material/download:",
        )
        
