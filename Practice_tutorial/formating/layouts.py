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


### Adds expander layout. Can hold multiple elements


st.markdown("----") 

st.header("Expander usage: st.expander")

with st.expander("Some explanation about expander"):
    st.write("""
        This inserts a container into your app tha can be used to hold multiple elements and 
        can be expanded or collapsed by the user. When collapsed, all that is visible 
        is the label.
        """)
    st.code("""
        # You can create a snippet of code hidden in the expander layout
    import pandas as
    import numpy as np

    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    """, language="python")

## Using containers

st.header("Container: st.container")
with st.container():
    st.write("You are inside the container")
    st.markdown("---")
    st.code("""
    # you can host multiple elements in the container
    import numpy as np
    y = np.arange(3, dtype=float)
    y
    """)
## Empty 
## Can hold a single element for a period of time and then 
# clear that element
st.markdown("---")
st.header("Empy: st.empty")

placeholder = st.empty()
for i in range(10):
    placeholder.write("This message will dissapear in {} seconds".format(11-i))
    time.sleep(1)
placeholder.empty()