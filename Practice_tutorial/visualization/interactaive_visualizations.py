"""
This python module outlines some examples of interactive visualization in streamlit
"""
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import os
import sys

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


sample = np.random.randint(low=10, high=20, size=(5,3))
sample= pd.DataFrame(sample, columns=['A','B','C'])
st.markdown("-----")
with st.container():
    st.write("Sample df")
    st.dataframe(sample)
    st.markdown("----------------")
    st.write("       bar_plot    ")
    st.bar_chart(sample)
    st.markdown("----------------")
    st.write("       area_plot    ")
    st.area_chart(sample)
    st.markdown("----------------")
    st.write("       line_plot    ")
    st.line_chart(sample)

st.markdown("-----")
data=pd.read_csv("../formating/tips.csv")
with st.container():
    st.header("Exploring plotly")
    st.markdown('----')
    st.write("1) Draw histogram for total bill")
    fig = px.histogram(data, x="total_bill")
    st.plotly_chart(fig)
    st.markdown('----')
    st.write("2) Draw histogram for total bill and color by sex")
    fig = px.histogram(data, x="total_bill", color="sex")
    st.plotly_chart(fig)
    st.markdown('----')
    st.write("3) Draw histogram for total bill and color by (sex, smoker, day, time)")
    select_color= st.selectbox("What category do you want to graph by",
                         ('sex','day','time'))
    fig = px.histogram(data, x="total_bill", color=select_color, title="Total bill count")
    st.plotly_chart(fig)
with st.container():
    st.markdown('----')
    st.write("4) Draw scatter plot between total_bill and tips and color by (sex, smoker, day, time)")
    color_option= st.selectbox('Select a category do you want to graph by', 
                               ('sex','day','time'))
    fig = px.scatter(data, x="total_bill", y="tip", color=color_option, title="Total bill count")
    st.plotly_chart(fig)


    