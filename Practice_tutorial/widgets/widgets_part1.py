"""
Practice module for input widgets in streamlit
"""
import streamlit as st
import pandas as pd
import numpy as np
import os
# If you click the button will perform a true or false action
#Create button widget
button = st.button("Button")
st.write('button = ', button)

#### Randomly display some rows of the csv when cliking the button
data=pd.read_csv("Practice_tutorial/formating/tips.csv")

def display_data_random(df):
    sample = df.sample(5)
    return sample
st.subheader("Displaying random 5 rows")
st.caption("Click on the button below to display the random sample rows")
button2 = st.button("Random sample")
if button2:
    sample = display_data_random(data)
    st.dataframe(sample)

# Checkbox
st.markdown("---")
st.subheader("st.checkbox")
#Returns a boolean value
agree= st.checkbox("I agree to terms and conditions")
st.write("Checkbox status=", agree)

# Creating multiple checkbox
st.markdown("---")
st.subheader("Multiple checkbox")
with st.container():
    st.info("What technologies you know")

    python =st.checkbox("Python")
    datascience=st.checkbox("Data Science")
    ai_ml = st.checkbox("AI/ML")
    R = st.checkbox("R")
    java= st.checkbox("Java")
    bayesian = st.checkbox("Bayesian statistics") 
    #Lets capture the info that the user checked
    tech_button = st.button("Submit")
    if tech_button:
        tech_dict = {
            'Python': python,
            'Data Science': datascience,
            'AI/ML': ai_ml,
            'R': R,
            'Java': java,
            'Bayesian statistics':bayesian
        }
        st.json(tech_dict)

# Radio button- in order to select one value out of several options

st.markdown("---")
st.subheader("st.radio")

radio_button = st.radio("What is your favorite color?",
                        ("White","Black","Pink","Red","Blue","Green"))

st.write("Your favorite color is {}".format(radio_button))

# Select box
st.markdown("---")
st.subheader("st.selectbox")
select_box= st.selectbox("What skill you want to learn most",
                         ('Java','Python','C++','Javascript','HTML','Others'))

st.write("You selected =", select_box)

## Multiselect box
st.markdown("---")
st.header("Multiselect")
# Returns the values of a list
options= st.multiselect("What type of movies you like:",
               ['Comedy','Action','Sci-fi','Drama','Romance']
               )
st.write('You selected',options)

## Sliders

st.markdown('---')
st.subheader("st.slider")
loan = st.slider("What is the loan amount you are looking for?", min_value=0, 
                 max_value=100000, step=1000)


st.write("The loan amount is ", loan)

