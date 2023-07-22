"""
This python module is the base for the data profilling app
"""
import streamlit as st
import pandas as pd
#from pandas_profiling import ProfileReport
#from streamlit_pandas_profiling import st_profile_report
import sys
import os

st.set_page_config(page_title='Data Profiler', layout='wide')

### Create a sidebar
with st.sidebar():
    uploaded_file = st.file_uploader("Upload .csv, .xlsx files not exceedig 10 MB")

if uploaded_file is not None:
    # time being let load csv
    df = pd.read_csv(uploaded_file)

    st.dataframe(df.head())
    # generate report
    with st.spinner('Generating Report'):
        pr = ProfileReport(df)

    st_profile_report(pr)
    



 
