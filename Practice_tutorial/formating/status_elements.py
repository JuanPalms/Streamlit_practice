"""
Python practice module for status elements in streamlit
"""

import streamlit as st
import time

### Progress bar
st.header("st.progress")
st.caption("Display a progress bar")

#You initialy provide a value, the progress bar ranges
#from 0 to 100 
my_bar=st.progress(50)

st.markdown("---")

# How dinamically change a progress bar
# with a for loop
st.header("st.progress dinamical")
st.caption("Displays a dinamical progress bar")
my_bar2=st.progress(0)
for pct_complete in range(1,101):
    time.sleep(0.5)
    my_bar2.progress(pct_complete)

st.markdown("---")

### Using spinners
st.header("st.spinner")
st.caption("Using spinners")


def a_progress_bar():
    for pct_complete in range(1,121,20):
        time.sleep(0.5)
        pct_complete=min(pct_complete,100)
        my_bar3.progress(pct_complete)

with st.spinner("Something is procerssing ..."):
    my_bar3 = st.progress(0)
    a_progress_bar()