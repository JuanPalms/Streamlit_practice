"""
Basic formating elements practice script
"""
import streamlit as st

#Formating a title
st.title("This is title")
st.caption("Using st.title you can display the text in title format")
# Headers and subheaders
st.header("This is Header 1")
st.caption('The text inside the header: Header 1')

#subheader
st.subheader("This is subheader")
st.caption('The text inside the subheader: subheader')

# Lets display code
st.markdown('---')
st.subheader('Generate code in Markdown')
body="""
import numpy as np

def generate_random(size):
    rand=np.random.random(size=size)
    return rand
number = generate_random(10)
"""
st.code(body, language='python')

## Lets display latex

st.markdown('---')
st.subheader('Displaying latex in Markdown')

formula= """

a + ar + ar^2 + ar^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} a r^k 
"""

st.latex(formula)

st.markdown("""
In order to know more about latex follow this link
<https://katex.org/>

""")


st.button("Rerun")