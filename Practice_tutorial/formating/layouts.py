"""
Python practice module of layouts in streamlit
"""
import streamlit as st
import pandas as pd
import time

### Adding sidebar layout
# creates the sidebar
side_bar = st.sidebar

#writes something in the sidebar
side_bar.header("Header 1")
side_bar.caption("This is a header inside the sidebar")
body_side_bar= """
--- 

Elements that are added to a sidebar are displayed in the left side

---
"""
side_bar.markdown(body_side_bar)
side_bar.write("This is a sidebar")

st.header("Header in principal page")
st.write("This input will be added in the princial page")

st.markdown("---")

df=pd.read_csv("Practice_tutorial/formating/tips.csv")
st.dataframe(data=df)

columns=tuple(df.columns)
st.write(columns)

# Create widget selectbox

select_column = side_bar.selectbox(
    "Select the column you want to display",
    columns
    )

side_bar.write('You selected the column name = {}'.format(select_column))

st.markdown("---")
### display the dataframe dinamically

st.dataframe(df[[select_column]])


st.markdown("---")

st.header('Columns: st.columns')
#Create 3 columns
col1, col2, col3 = st.columns(3)
# in order to insert digits in the columns
with col1:
    st.subheader('Column 1')
    st.image("Practice_tutorial/formating/image.jpg")

with col2:
    st.subheader('Column 2')
    st.dataframe(data=df)

with col3: 
    st.subheader("Column 3")
    st.dataframe(df[[select_column]])



