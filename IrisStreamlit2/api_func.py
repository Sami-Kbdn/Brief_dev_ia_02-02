from fastapi import FastAPI
import numpy as np 
from train_model import make_model_save
from make_pred import make_prediction

app = FastAPI()

@app.get('/infos')
def read_root():
    return {"message" : "Hello, welcome on my dashbord!"}

@app.get('/train_model')
def train_model():
    make_model_save()
    print ('training in progress')
    return {"Response":'Training completed.'}

@app.get("/{x1}/{x2}/{x3}/{x4}")
def get_pred(x1: float, x2: float, x3: float, x4: float):
    p1 = [x1, x2, x3, x4]
    x = np.array([p1])
    print('x', x)

    prediction = make_prediction(x)

    print(prediction)

    return {"prediction": prediction}