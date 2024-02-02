import streamlit as st
import pandas as pd 
import plotly.express as px 

df = pd.read_csv("iris_data.csv")

st.set_page_config(page_title="Iris Dataset")
st.header("Values - Iris Dataset")
st.markdown("Explore the variables to understand the relationship between them and how they relate to the species.")
st.sidebar.header("Individual Values")

options = st.sidebar.radio("Select values",
                           options=["sepal_length", "sepal_width", "petal_length", "petal_width"])

show_df = df.filter(items=[options, "species"])

plot1 = px.histogram(
    show_df,
    x=show_df[options],
    title=f"{options} Histogram",
    nbins = 30,
    color="species")

st.plotly_chart(plot1)

print(show_df.shape)