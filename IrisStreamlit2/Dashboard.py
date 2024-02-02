import streamlit as st
import pandas as pd 

df = pd.read_csv("iris_data.csv")

st.set_page_config(page_title="Iris Dataset")
st.header("Iris Machine Learning Project")
st.markdown("Deployment of the Iris dataset machine learning model using XGBoost.")
st.markdown("Use this dashboard to understand the data and to make predictions.")
st.markdown("")
st.image("img.png")