"""
Practice module for visualization with matplotlib and stramlit
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

data=pd.read_csv("../formating/tips.csv")

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
    st.markdown("---")
    #draw bar plot
    fig,ax = plt.subplots()
    ax.bar(['Male','Female'],value_counts)
    st.pyplot(fig)
    # put this in an expander
    st.dataframe(value_counts)

## Using layout to display the column side by side
with st.container():
    st.subheader("Displaying side by side")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Pie chart")
        st.write("1) Find the number of Male and Female distribution")
        #draw pie chart
        fig,ax = plt.subplots()
        ax.pie(value_counts,autopct="%0.2f%%", labels= ["Male", "Female"])
        ax.set_title("Male and female distribution")
        st.pyplot(fig)
    with col2: 
        st.subheader("Plotting a bar plot instead")
        fig, ax = plt.subplots()
        ax.bar(['Male','Female'], value_counts)
        st.pyplot(fig)  
    with st.expander('Click here to display value counts'):
        st.dataframe(value_counts)

### using streamlit widgets
data_types =data.dtypes
cat_cols = tuple(data_types[data_types == 'object'].index)
st.markdown("---")
with st.container():
    st.subheader("Controling graphs with widgets")
    feature = st.selectbox('Select the feature you want to display bar and pie chart',
                           cat_cols)
    value_counts = data[feature].value_counts()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Pie chart")
        st.write(f"1) Find the number of {feature} distribution")
        #draw pie chart
        fig,ax = plt.subplots()
        ax.pie(value_counts,autopct="%0.2f%%", labels= value_counts.index)
        ax.set_title(f"{feature} distribution")
        st.pyplot(fig)
    with col2: 
        st.subheader("Plotting a bar plot instead")
        fig, ax = plt.subplots()
        ax.bar(value_counts.index, value_counts)
        st.pyplot(fig)  
    with st.expander('Click here to display value counts'):
        st.dataframe(value_counts)



#2) Find the distribution of Male and Female spent (boxplot or kdeplot)
st.subheader("Boxplot and kdeplot")
st.markdown("---")
with st.container():
    st.write('2. Find the distribution of Male and Female spent')
    ##### selectiong dinamically the chart to display
    chart = ('box','violin','kdeplot', 'histogram')
    ## Create a selection option
    chart_selection = st.selectbox('Select the chart type', chart)
    fig, ax = plt.subplots()
    if chart_selection == 'box':
        sns.boxplot(x='sex', y='total_bill', data= data, ax=ax)
    elif chart_selection == 'violin':
        sns.violinplot(x='sex', y='total_bill', data= data, ax=ax)
    elif chart_selection == 'kdeplot':
        sns.kdeplot(x=data['total_bill'], hue=data['sex'], ax=ax)
    else:
        sns.histplot(x='total_bill', hue='sex', data=data, ax=ax)
    st.pyplot(fig)
    
    
    

#3) Find the distribution of average total_bill across each day by male and female

st.subheader("")
st.markdown("---")
features_to_gropby = ['day','sex']
feature =['total_bill']
select_cols = feature+features_to_gropby
avg_total_bill = data[select_cols].groupby(features_to_gropby).mean()
avg_total_bill = avg_total_bill.unstack()

### Visualization
fig, ax = plt.subplots()
avg_total_bill.plot(kind='bar', ax=ax)

st.pyplot(fig)
st.dataframe(avg_total_bill) 

st.subheader("")
st.markdown("---")
with st.container():
    #1. Include all categorical features
    #2. Bar, area and line
    #3. Stacked bar
    c1, c2, c3 = st.columns(3)
    with c1: 
        group_cols = st.multiselect('select the features',cat_cols, cat_cols[0])
        features_to_gropby = group_cols
        n_features = len(features_to_gropby)
    with c2:
        chart_type = st.selectbox('Select Chart type', ('bar','area','line'))
    with c3:
        stack_option = st.radio('Stacked',('Yes','No'))
        if stack_option == 'Yes':
            stacked = True
        else:
            stacked = False
            
    feature =['total_bill']
    select_cols = feature+features_to_gropby
    avg_total_bill = data[select_cols].groupby(features_to_gropby).mean()
    if n_features >1:
        for i in range(n_features-1):
            avg_total_bill = avg_total_bill.unstack()
    
    ### Visualization
    fig, ax = plt.subplots()
    avg_total_bill.plot(kind=chart_type, ax=ax, stacked=stacked)
    ax.set_ylabel('Avg total bill')
    st.pyplot(fig)
    with st.expander('Click here to display values'):
        st.dataframe(avg_total_bill)   


#4) Find the relation between total_bill and tip on time (scatter plot)
st.markdown("-----")
st.markdown("scatter plot")
with st.container():
    st.write("Find the relation between total_bill and tip on time (scatter plot)")
    fig, ax = plt.subplots()
    hue_type = st.selectbox('Select the feature to hue', cat_cols)
    sns.scatterplot(x='total_bill',y='tip',hue=hue_type,ax=ax, data=data)
    st.pyplot(fig)




st.button("Rerun")


