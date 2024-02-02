import streamlit as st
import pandas as pd 
import plotly.express as px 

df = pd.read_csv("iris_data.csv")

st.set_page_config(page_title="Iris Dataset")
st.header("Comparaison - Iris Dataset")
st.markdown("Explore the variables to understand the relationship between them and how they relate to the species.")
st.sidebar.header("Variable Comparaison")

options = st.sidebar.radio("Select comparaison",
                           options=["Sepal Length Vs Sepal Width",
                                    "Petal Length Vs Petal Width",
                                    "Sepal Length Vs Petal Width",
                                    "Sepal Width Vs Petal Length"])

if options == "Sepal Length Vs Sepal Width":
    st.markdown('option1')
elif options == "Petal Length Vs Petal Width":
    st.markdown('option2')
elif options == "Sepal Length Vs Petal Width":
    st.markdown('option3')
elif options == "Sepal Width Vs Petal Length":
    st.markdown('option4')


if options == "Sepal Length Vs Sepal Width":
    plot = px.scatter(
        df,
        x="sepal_length",
        y="sepal_width",
        color="species",
        title=options)


elif options == "Petal Length Vs Petal Width":
    plot = px.scatter(
        df,
        x="petal_length",
        y="petal_width",
        color="species",
        title=options)


elif options == "Sepal Length Vs Petal Width":
    plot = px.scatter(
        df,
        x="sepal_length",
        y="petal_width",
        color="species",
        title=options)


elif options == "Sepal Width Vs Petal Length":
    plot = px.scatter(
        df,
        x="sepal_width",
        y="petal_length",
        color="species",
        title=options)
    

st.plotly_chart(plot)


    