"""
Practice module for displaying and usign data formats in 
streamlit web app
"""

import streamlit as st
import pandas as pd
import numpy as np

df=pd.read_csv("Practice_tutorial/formating/tips.csv")
st.header("Displaying DataFrame with magic")
df
st.markdown("---")
st.header("st.dataframe")
st.caption("Display DataFrame as interactive element")
# we can add parameters for the size of the interactive table
# that we want to display
st.dataframe(data=df, width=200, height=100)

st.markdown("---")
st.header("st.table")
st.caption("Displays an static table")
st.table(data=df.head(5) )

### Displaying data in JSON format
## 1) Take first 5 rows and convert them as JSON
st.markdown("---")
st.header("st.json")
st.caption("Display object or string as pretty printed JSON string")

json_values=df.head(3).to_dict()
st.json(json_values)


st.button("Rerun")
