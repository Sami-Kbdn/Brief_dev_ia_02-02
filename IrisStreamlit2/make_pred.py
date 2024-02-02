import json
import pickle

def make_prediction(x):
    # charger modèle à partir fichier pickle
    with open ('main_model.pkl', 'rb') as fichier_modele:
        loaded_model = pickle.load(fichier_modele)

    predictions_out = loaded_model.predict(x)

    print('prediction:', predictions_out)


    with open('encoder.json') as json_file:
        data = json.load(json_file)
    
    predictions_string = data[str(int(predictions_out))]

    return predictions_string
    



    # dict_out = {}
    # for count, value in enumerate (predictions_out):
    #     dict_out[count] = float(value)
    