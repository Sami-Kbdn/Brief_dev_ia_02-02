import streamlit as st 
import numpy as np  
from make_pred import make_prediction
import json
import pandas as pd
import plotly_express as px 
import requests

df = pd.read_csv("iris_data.csv")

st.set_page_config(page_title="Prediction")
st.header("Prediction - Iris Dataset")
st.markdown("Using RandomForestClassifier, make predictions")
st.sidebar.header("Make Prediction")

sep_len = st.sidebar.text_input("Sepal Length")
sep_wid = st.sidebar.text_input("Sepal Width")
pet_len = st.sidebar.text_input("Petal Length")
pet_wid = st.sidebar.text_input("Petal Width")
make_pred_API = st.sidebar.button("Predict")

# with open('encoded.json') as json_file:
#     data = json.load(json_file)


plot1 = px.scatter(
    df,
    x = "sepal_length",
    y = "petal_width",
    title = "Sepal Length vs Petal Width",
    color = "species")

plot2 = px.scatter(
    df,
    x = "sepal_length",
    y = "petal_length",
    title = "Sepal Length vs Petal Length",
    color = "species")



if make_pred_API:
    url = f"http://localhost:8000/{float(sep_len)}/{float(sep_wid)}/{float(pet_len)}/{float(pet_wid)}"

    response = requests.get(url)

    if response.status_code == 200:
        species_pred = response.json()["prediction"]
        st.success(f"Prediction result: {species_pred}")
    else :
        st.error("Error in prediction request")
    
    p1 = [float(sep_len), float(sep_wid), float(pet_len), float(pet_wid)]
    x = np.array([p1])
    row = {"sepal_length" : [float(sep_len)],
           "sepal_width" : [float(sep_wid)],
           "petal_length" : [float(pet_len)],
           "petal_width" : [float(pet_wid)]}
    
    p1_df = pd.DataFrame(row)

    plot1.add_scatter(x=p1_df["petal_length"],
                      y=p1_df["petal_width"],
                      mode = 'markers',
                      name = species_pred,
                      marker=dict(
                          color = 'red',
                          size = 10,
                          symbol='circle',
                          line=dict(
                              color='white',
                              width=2
                          )
                      ))
    
    plot2.add_scatter(x=p1_df["sepal_length"],
                      y=p1_df["sepal_width"],
                      mode = 'markers',
                      name = species_pred,
                      marker=dict(
                          color = 'red',
                          size = 10,
                          symbol='circle',
                          line=dict(
                              color='white',
                              width=2
                          )
                      ))

st.plotly_chart(plot1)
st.plotly_chart(plot2)
