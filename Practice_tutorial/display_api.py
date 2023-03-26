"""This module reproduces the content of the course in 
streamlit, section 2"""
import streamlit as st
import pandas as pd
import numpy as np

# You can display almost anything just by passing it to 
# st.write()

st.write("Hello world")
st.write("Welcome to Streamlit App APIs")
st.write(1234)
df=pd.DataFrame({
    "first_column":[1,2,3,4,5],
    "second_column":["a","b","c","d","e"],
    "third_column":[12.1,12.34,12.33,15.1, 66]
}
)
st.write(df)
st.write(np.array([1,2,3,4]))

## --------- MAGIC ---------------#
st.write("Magic commands")
df1=pd.DataFrame({'col1':[1,2,3]})

df1

x=10

x

st.button("Rerun")
