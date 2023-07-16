"""
Python module of practice of widgets in streamlit
"""
import streamlit as st

st.markdown('----')
st.subheader('st.slider')
loan = st.slider(
    'What is  the loan amount you are looking for?',0,1000000, 1000, 1000
)
st.write('Loan mount=',loan)

st.markdown('----')
st.subheader('st.text_input','st.number_input')

with st.container():
    name= st.text_input('Please enter your name')
    age= st.number_input('What is your age?', min_value=0, max_value=150, value=30, step=1)
    describe = st.text_area('Writing area',height=150)
    dob = st.date_input('Select date of birth')

    submit_button = st.button('Submit')

    if submit_button:
        info ={
            "Name":name,
            "Age":age,
            "Data of birth": dob,
            "About Yourself": describe
        }
        st.json(info)



