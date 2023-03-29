"""
Practice module for visualization with matplotlib and stramlit
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Practice_tutorial/formating/tips.csv")

st.header("Matplotlib and seaborn visualization in streamlit")
st.dataframe(data.head())
st.markdown("---")
#Data questions
# 1) Find the number of Male and Female distribution (pie chart)
with st.container():
    st.subheader("Pie bar")
    st.write("1) Find the number of Male and Female distribution")
    value_counts = data["sex"].value_counts()
    #draw pie chart
    fig,ax = plt.subplots()
    ax.pie(value_counts,autopct="%0.2f%%", labels= ["Male", "Female"])
    ax.set_title("Male and female distribution")
    st.pyplot(fig)
    #draw bar plot
    fig,ax = plt.subplots()
    # put this in an expander
    st.dataframe(value_counts)



st.markdown("---")
#2) Find the distribution of Male and Female spent (boxplot or kdeplot)
st.subheader("Boxplot and kdeplot")
st.markdown("---")
#3) Find the distribution of average total_bill across each day by male and female

st.subheader("")
st.markdown("---")
#4) Find the relation between total_bill and tip on time (scatter plot)
st.markdown("scatter plot")


st.button("Rerun")