import pandas as pd
from flask import Flask,render_template,request,send_file
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib
app = Flask(__name__)
@app.route('/')
def prediction_fun():
    # Load the CSV file
    data = pd.read_csv('diabetes.csv')   # Reading the Diabetes.csv File Using the pandas 

    # Separate features (X) and target (y)
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']

    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create and train a logistic regression model
    model = LogisticRegression()
    model.fit(X_scaled, y)

    # Saving the tranied model 
    joblib.dump(model, 'diabetes_model.pkl')    # The Model is saved into diabetes_model.pkl   i.e pickle 

    # Load the model
    loaded_model = joblib.load('diabetes_model.pkl')  # The Save model which is in the diabetes_model.pkl  is now loaded in loaded_model variable 

    # Get user input for feature values
    pregnancies = float(6)
    glucose = float(148)
    blood_pressure = float(72)
    skin_thickness = float(35)
    insulin = float(0)
    bmi = float(33.6)
    diabetes_pedigree = float(0.627)
    age = float(50)

    # Prepare input data for prediction   
    # Creating an array using the numpy
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    input_data_scaled = scaler.transform(input_data)

    # Predict using the loaded model
    prediction = loaded_model.predict(input_data_scaled)

    # Print the prediction result
    if prediction[0] == 0:
        return "Based on the provided information, you are predicted to be non-diabetic."
    else:
        return "Based on the provided information, you are predicted to have diabetes."
if __name__=="__main__":
    app.run(debug=True,port="2006")