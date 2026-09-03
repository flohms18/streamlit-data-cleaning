import streamlit as st
import pandas as pd

MyDf = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column': [10, 20, 30,40]
})

def hello():
    print(MyDf)

hello()