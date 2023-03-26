"""
This is a practice module that builds an app with streamlit
library
"""
#imports
import streamlit as st
import time
import numpy as np
#returns the version of streamlit
# Use st.write to write an output to the app
st.write("streamlit version is {}".format(st.__version__))

# Design a progress bar
progress_bar=st.sidebar.progress(0)
status_text=st.sidebar.empty()

# create data
last_rows=np.random.randn(1,1)
# In a single line create a line chart just pass the data
chart=st.line_chart(last_rows)
# for loop to progress bar
for i in range(1,101):
    new_rows = last_rows[-1,:] + np.random.randn(5,1).cumsum(axis=0)
    status_text.text("%i%% Complete"%i)
    progress_bar.progress(i)
    chart.add_rows(new_rows)
    last_rows=new_rows

    time.sleep(0.1)

progress_bar.empty()

st.button("Rerun")